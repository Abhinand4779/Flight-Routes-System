from django.db import models

class AirportRoute(models.Model):
   
    # Routes are structured as a tree where each node can have a 'left' or 'right' child.

    POSITION_CHOICES=[
        ('left','Left'),
        ('right','Right'),
    ]
    
    airport_code=models.CharField(max_length=10, unique=True, verbose_name="Airport Code")
    parent=models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name="Parent Airport"
    )
    position=models.CharField(
        max_length=10, 
        choices=POSITION_CHOICES, 
        null=True, 
        blank=True,
        verbose_name="Position"
    )
    duration=models.IntegerField(help_text="Duration from parent to this node in minutes/km")

    def __str__(self):
        return self.airport_code

    class Meta:
        unique_together=('parent','position')
        verbose_name="Airport Route"
        verbose_name_plural="Airport Routes"

    def get_path_to_root(self):

        # Returns a list of nodes from this node up to the root for path calculations.

        path=[]
        curr=self
        while curr:
            path.append(curr)
            curr = curr.parent
        return path

    @classmethod
    def find_shortest_path(cls,code1,code2):
        
        # the Shortest path based on duration between two airports.

        # Uses Lowest Common Ancestor (LCA) to calculate the route.
        
        n1=cls.objects.filter(airport_code__iexact=code1).first()
        n2=cls.objects.filter(airport_code__iexact=code2).first()
        
        if not n1 or not n2:
            return None, "One or both airport codes not found in the system."
            
        p1=n1.get_path_to_root()
        p2=n2.get_path_to_root()
        
        # To Find Lowest Common Ancestor (LCA)

        lca=None
        for node in p1:
            if node in p2:
                lca=node
                break
        
        if not lca:
            return None, "No common route exists between these two airports."
            
        total_duration=0
        path_names=[]
        
        # To Traverse from first airport up to LCA

        curr=n1
        while curr !=lca:
            total_duration+=curr.duration
            path_names.append(curr.airport_code)
            curr=curr.parent
        
        path_names.append(lca.airport_code)
        
        # To Traverse from LCA down to second airport

        temp_path = []
        curr = n2
        while curr !=lca:
            total_duration += curr.duration
            temp_path.append(curr.airport_code)
            curr=curr.parent
            
        path_names.extend(reversed(temp_path))
        
        return {
            'duration':total_duration,
            'path': " -> ".join(path_names)
        }, None

    def get_longest_path_info(self):
        
    #    the longest duration path from this node.
        
        children=self.children.all()
        if not children.exists():
            return 0,[self.airport_code]
        
        max_d=-1
        best_path=[]
        
        for child in children:
            d,path=child.get_longest_path_info()
            current_total=d+child.duration
            if current_total > max_d:
                max_d=current_total
                best_path=[self.airport_code] + path
                
        return max_d,best_path

    @classmethod
    def get_nth_node(cls,start_node,n,direction):

        # To Traverses N times in a given position/direction.
            
        curr=start_node
        for _ in range(n):
            next_node=cls.objects.filter(parent=curr, position=direction).first()
            if next_node:
                curr=next_node
            else:
                return None
        return curr
