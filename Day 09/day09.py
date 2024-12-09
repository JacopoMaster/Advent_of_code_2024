def parse_disk_map(disk_map_str):
    # Parse the disk map into segments of ('file', length, file_id) and ('free', length)
    lengths = list(map(int, disk_map_str.strip()))
    segments = []
    i = 0
    file_id = 0
    while i < len(lengths):
        file_len = lengths[i]
        i += 1
        # File segment
        segments.append(('file', file_len, file_id))
        file_id += 1
        if i < len(lengths):
            free_len = lengths[i]
            i += 1
            if free_len > 0:
                segments.append(('free', free_len))
    return segments

def build_disk(segments):
    # Build the disk as a list of characters: file blocks are digits, free space is '.'
    disk = []
    for seg in segments:
        if seg[0] == 'file':
            _, length, fid = seg
            disk.extend([str(fid)] * length)
        else:
            _, length = seg
            disk.extend(['.'] * length)
    return disk

def compute_checksum(disk):
    # Compute checksum: sum of (position * file_id) for each file block
    total = 0
    for pos, ch in enumerate(disk):
        if ch.isdigit():
            fid = int(ch)
            total += pos * fid
    return total

########################################
# Part 1: moving blocks one by one
########################################
def compact_part_one(disk):
    # Compact by moving one file block at a time from the right to the leftmost '.' that occurs before any file block.
    # Repeat until no '.' lies to the left of a file block.
    while True:
        dot_index = None
        for idx in range(len(disk)):
            if disk[idx] == '.':
                # Check if there's a file block to the right
                if any(ch != '.' for ch in disk[idx+1:]):
                    dot_index = idx
                    break
        if dot_index is None:
            # No '.' that has a file block to the right => fully compacted
            break

        # Find the last file block on the right
        file_index = None
        for idx in range(len(disk)-1, -1, -1):
            if disk[idx] != '.':
                file_index = idx
                break

        # Swap the file block with the dot
        disk[dot_index], disk[file_index] = disk[file_index], disk[dot_index]
    return disk

########################################
# Part 2: moving whole files at once
########################################
def find_files(disk):
    files = {}
    current_id = None
    current_start = None
    for i, ch in enumerate(disk):
        if ch.isdigit():
            fid = int(ch)
            if current_id is None:
                current_id = fid
                current_start = i
            else:
                if fid != current_id:
                    # close previous file
                    files[current_id] = {
                        'id': current_id,
                        'start': current_start,
                        'end': i - 1,
                        'length': (i - 1) - current_start + 1
                    }
                    # start new file
                    current_id = fid
                    current_start = i
        else:
            if current_id is not None:
                files[current_id] = {
                    'id': current_id,
                    'start': current_start,
                    'end': i - 1,
                    'length': (i - 1) - current_start + 1
                }
                current_id = None
                current_start = None
    if current_id is not None:
        # close last file
        files[current_id] = {
            'id': current_id,
            'start': current_start,
            'end': len(disk) - 1,
            'length': (len(disk) - 1) - current_start + 1
        }
    return files

def find_free_spans(disk):
    free_spans = []
    in_free = False
    start_free = None
    for i, ch in enumerate(disk):
        if ch == '.' and not in_free:
            in_free = True
            start_free = i
        elif ch != '.' and in_free:
            free_spans.append((start_free, i - 1))
            in_free = False
    if in_free:
        free_spans.append((start_free, len(disk) - 1))
    return free_spans

def can_move_file_whole(disk, file_info):
    # Look for a free span to the LEFT of file_info['start'] that can fit the entire file
    length_needed = file_info['length']
    file_start = file_info['start']
    free_spans = find_free_spans(disk)
    left_spans = [span for span in free_spans if span[1] < file_start]
    for (fs, fe) in left_spans:
        span_len = fe - fs + 1
        if span_len >= length_needed:
            return (fs, fs + length_needed - 1)
    return None

def move_file(disk, file_info, new_start, new_end):
    file_blocks = disk[file_info['start']:file_info['end']+1]
    for i in range(new_start, new_end+1):
        disk[i] = file_blocks[i - new_start]
    for i in range(file_info['start'], file_info['end']+1):
        disk[i] = '.'

def compact_part_two(disk):
    files = find_files(disk)
    file_ids = sorted(files.keys(), reverse=True)
    for fid in file_ids:
        file_info = files[fid]
        span = can_move_file_whole(disk, file_info)
        if span is not None:
            new_start, new_end = span
            move_file(disk, file_info, new_start, new_end)
            # Update file info (not strictly necessary for final outcome)
            files[fid]['start'] = new_start
            files[fid]['end'] = new_end
    return disk




########################################
# Main
########################################
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        disk_map_str = f.read().strip()

    # Part 1
    segments = parse_disk_map(disk_map_str)
    disk_part_one = build_disk(segments[:])  # copy of segments
    
    disk_part_one = compact_part_one(disk_part_one)
    checksum_part_one = compute_checksum(disk_part_one)

    # Part 2
    segments = parse_disk_map(disk_map_str)
    disk_part_two = build_disk(segments[:])  # copy of segments
    
    disk_part_two = compact_part_two(disk_part_two)
    checksum_part_two = compute_checksum(disk_part_two)

    
    print("Part One (moving blocks individually) checksum:", checksum_part_one, "🎅✨")
    print("Part Two (moving whole files) checksum:", checksum_part_two, "🎄🎁")

