import (
	"container/heap"
	"fmt"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // Max Heap
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func solution(n int, k int, enemy []int) int {
	h := &IntHeap{}
	for i, v := range enemy {
		heap.Push(h, v)
		n -= v
		if n >= 0 {
			continue
		} else if k > 0 {
			for k > 0 && n < 0 && len(*h) > 0 {
				n += heap.Pop(h).(int)
				k--
			}
			if n >= 0 {
				continue
			} else {
				return i
			}
		} else {
			return i
		}
	}
	return len(enemy)
}
