import sys

CHUNK_COUNT = 8

def get_all_chunks(addr):
    chunks = addr.split(":")
    if "::" not in addr:
        return chunks
    
    pad_chunk_cnt = CHUNK_COUNT - (len(chunks) - 1)
    partition_idx = chunks.index("")
    return chunks[:partition_idx] + ["" for _ in range(pad_chunk_cnt)] + chunks[partition_idx+1:]
    

def solution(addr):
    full_addr = get_all_chunks(addr)

    for i, chunk in enumerate(full_addr):
        full_chunk = "0" * (4 - len(chunk)) + chunk
        full_addr[i] = full_chunk

    return ":".join(full_addr)


if __name__ == "__main__":
    addr = sys.stdin.readline().strip()
    print(solution(addr))