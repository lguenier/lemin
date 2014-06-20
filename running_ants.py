def lets_run(paths, mouse_count):
    count_path_len(paths)
    while mouse_count > 0:
        

def count_path_len(paths):
    path_len = []
    i = 0
    while i < len(paths):
        path_len.append(len(paths[i][1:-1]))
        i += 1
    return path_len
