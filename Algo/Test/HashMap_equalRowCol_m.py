def num_equal_pairs_optimized(grid):
    n = len(grid)
    count = 0

    # Hash maps to store the rows and columns
    row_map = {}
    col_map = {}

    for i in range(n):
        # Convert the row and column lists to tuples for hashability
        row_tuple = tuple(grid[i])
        col_tuple = tuple(grid[j][i] for j in range(n))
        #print(col_tuple)
        # Increment count if the row or column is already encountered
        count += row_map.get(row_tuple, 0)
        count += col_map.get(col_tuple, 0)

        # Update hash maps
        row_map[row_tuple] = row_map.get(row_tuple, 0) + 1
        col_map[col_tuple] = col_map.get(col_tuple, 0) + 1

        print("rmap",row_map[row_tuple])

    return count

# Example usage:
grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
output1 = num_equal_pairs_optimized(grid1)
print(output1)  # Output: 1
