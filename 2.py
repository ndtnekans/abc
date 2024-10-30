import numpy as np

# Kiểm tra trạng thái hiện tại có phải là lời giải hợp lệ không
def is_valid_state(state, num_queens):
    return len(state) == num_queens

# Tìm các vị trí hợp lệ tiếp theo cho quân hậu
def get_candidates(state, num_queens):
    if not state:
        return range(num_queens)
    
    position = len(state)
    candidates = set(range(num_queens))
    
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    
    return candidates

# Đệ quy thực hiện tìm kiếm theo chiều sâu để tìm các lời giải hợp lệ
def search(state, solutions, num_queens):
    if is_valid_state(state, num_queens):
        solutions.append(state.copy())
        print(f"Valid State Found: {state}")
    
    for candidate in get_candidates(state, num_queens):
        state.append(candidate)
        search(state, solutions, num_queens)
        print(f"Backtracking from: {state}")
        state.remove(candidate)

# Chạy chương trình tìm lời giải
if __name__ == "__main__":
    num_queens = 3
    solutions = []
    search([], solutions, num_queens)
    print(f"Total Solutions: {len(solutions)}")
    import numpy as np

def solve(num_queens):
    solutions = []
    state = []
    search(state, solutions, num_queens)
    return solutions

if __name__ == "__main__":
    num_queens = int(input("Enter number of queens: "))
    solutions = solve(num_queens)
    for solution in solutions:
        board = np.full((num_queens, num_queens), "-")
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        print(f'\nSolution: {solution}')
        print(board)