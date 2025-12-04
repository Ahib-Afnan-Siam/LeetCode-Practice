class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for car in directions:
            if car == 'R':
                stack.append('R')
            elif car == 'S':
                # All preceding 'R's will collide with this stationary car
                while stack and stack[-1] == 'R':
                    collisions += 1
                    stack.pop()
                stack.append('S')
            else:  # car == 'L'
                if stack:
                    if stack[-1] == 'R':
                        # Head-on collision
                        collisions += 2
                        stack.pop()
                        # Remaining 'R's will collide with the resulting stationary cluster
                        while stack and stack[-1] == 'R':
                            collisions += 1
                            stack.pop()
                        # The cluster becomes stationary
                        stack.append('S')
                    else:  # stack[-1] == 'S'
                        # Moving 'L' hits a stationary cluster
                        collisions += 1
                        # 'L' becomes part of the cluster, so no change to stack
                # If stack is empty, this 'L' never collides
        
        return collisions