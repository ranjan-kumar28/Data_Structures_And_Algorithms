void pre(Node* root, map<int, pair<int,int>> &comb, int hd, int vd){
    if(comb.find(hd)==comb.end()) comb[hd] = make_pair(root->data, vd);
    else if(comb[hd].second <= vd) {comb[hd].second = vd; comb[hd].first = root->data;}
    if(root->left) pre(root->left, comb, hd-1, vd+1);
    if(root->right) pre(root->right, comb, hd+1, vd+1);
}

vector<int> bottomView(Node *root){ 
    if (root == NULL) return vector<int>(0); 
    map<int, pair<int,int>> comb;
    pre(root, comb, 0, 0);
    vector<int> res;
    for(auto it=comb.begin(); it!=comb.end(); it++) res.push_back((it->second).first);
    return res;
}
