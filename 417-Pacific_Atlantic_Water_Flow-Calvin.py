class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pacificFlow = [[False] * cols for _ in range(rows)]
        atlanticFlow = [[False] * cols for _ in range(rows)]


        def dfs(xPos: int, yPos: int, flow: List[List[False]]) :
            currentHeight = heights[xPos][yPos]
            flow[xPos][yPos] = True

            # Check down
            if (
                xPos + 1 < rows and # Check bounds
                heights[xPos + 1][yPos] >= currentHeight and # Water can flow from next to current cell
                flow[xPos + 1][yPos] == False
            ):
                dfs(xPos + 1, yPos, flow)
            
            # Check up
            if (
                xPos - 1 >= 0 and # Check bounds
                heights[xPos - 1][yPos] >= currentHeight and # Water can flow from next to current cell
                flow[xPos - 1][yPos] == False
            ):
                dfs(xPos - 1, yPos, flow)
            
            # Check right
            if (
                yPos + 1 < cols and # Check bounds
                heights[xPos][yPos + 1] >= currentHeight and # Water can flow from next to current cell
                flow[xPos][yPos + 1] == False
            ):
                dfs(xPos, yPos + 1, flow)
            
            # Check left
            if (
                yPos - 1 >= 0 and # Check bounds
                heights[xPos][yPos - 1] >= currentHeight and # Water can flow from next to current cell
                flow[xPos][yPos - 1] == False
            ):
                dfs(xPos, yPos - 1, flow)

        for col in range(cols):
            dfs(0, col, pacificFlow)
            dfs(rows - 1, col, atlanticFlow)
        for row in range(rows):
            dfs(row, 0, pacificFlow)
            dfs(row, cols - 1, atlanticFlow)

        results = []

        for row in range(rows) :
            for col in range(cols) :
                if pacificFlow[row][col] and atlanticFlow[row][col] :
                    results.append([row,col])

        return results