class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def recursiveLands(xPos: int, yPos: int) :
            grid[xPos][yPos] = '2'
            if ( # Check Down
                xPos + 1 < rows and  # Check if within bounds (down)
                grid[xPos + 1][yPos] != '2' and # Not visited
                grid[xPos + 1][yPos] == '1'   # Same type as current
            ):
                recursiveLands(xPos + 1, yPos)
            if ( # Check Up
                xPos - 1 >= 0 and  # Check if within bounds (up)
                grid[xPos - 1][yPos] != '2' and # Not visited
                grid[xPos - 1][yPos] == '1'   # Same type as current
            ):
                recursiveLands(xPos - 1, yPos)
            if ( # Check Right
                yPos + 1 < len(grid[0]) and  # Check if within bounds (right)
                grid[xPos][yPos + 1] != '2' and # Not visited
                grid[xPos][yPos + 1] == '1'   # Same type as current
            ):
                recursiveLands(xPos, yPos + 1)
            if ( # Check Left
                yPos - 1 >= 0 and  # Check if within bounds (left)
                grid[xPos][yPos - 1] != '2' and # Not visited
                grid[xPos][yPos - 1] == '1'   # Same type as current
            ):
                recursiveLands(xPos, yPos - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' : 
                    recursiveLands(row, col) 
                    islands += 1

        return islands
        