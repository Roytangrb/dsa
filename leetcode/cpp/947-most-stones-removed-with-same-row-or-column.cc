// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

#include <iostream>
#include <vector>
#include <unordered_set>

using std::vector;
using std::cout;
using std::unordered_set;

int find(vector<int>& parent, int x) {
  if (parent[x] == -1) {
    parent[x] = x;
  }
  if (parent[x] == x) {
    return parent[x];
  }
  return parent[x] = find(parent, parent[x]);
}

void union_stones(vector<int>& parent, vector<int>& size, int x, int y) {
  int px = find(parent, x);
  int py = find(parent, y);
  if (px == py) return;

  int sx = size[px];
  int sy = size[py];
  if (sx < sy) {
    parent[px] = py;
    size[py] += sx;
  } else {
    parent[py] = px;
    size[px] += sy;
  }
}

int removeStones(const vector<vector<int>>& stones) {
  int n = stones.size();
  vector<int> parent(n, -1);
  vector<int> size(n , 1);
  for (int i = 0; i < n; i ++) {
    for (int j = i+1; j < n; j ++) {
      if (stones[i][0] == stones[j][0]
          || stones[i][1] == stones[j][1]) {
        union_stones(parent, size, i, j);
      }
    }
  }

  int comp_count = 0;
  unordered_set<int> components;
  for (int i = 0; i < n; i++) {
    int comp = find(parent, i);
    if (!components.contains(comp)) {
      comp_count ++;
      components.insert(comp);
    }
  }

  return n - comp_count;
}

int main() {
  vector<vector<int>> stones1 = {{0,0},{0,1},{1,0},{1,2},{2,1},{2,2}};
  cout << removeStones(stones1) << '\n';
  vector<vector<int>> stones2 = {{0,0},{0,2},{1,1},{2,0},{2,2}};
  cout << removeStones(stones2) << '\n';
  vector<vector<int>> stones3 = {{0,0}};
  cout << removeStones(stones3) << '\n';
  vector<vector<int>> stones4 = {{0,1},{1,2},{1,3},{3,3},{2,3},{0,2}};
  cout << removeStones(stones4) << '\n';
}
