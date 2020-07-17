Node* LCA(Node *root, int a, int b){
    if(!root) return NULL;
    if(root->data == a || root->data == b) return root;
    Node *l = NULL, *r = NULL;
    l = LCA(root->left ,a ,b);
    if(l && l->data!=a && l->data!=b) return l;
    r = LCA(root->right ,a ,b);
    if(r && r->data!=a && r->data!=b) return r;
    if(l && !r) return l;
    else if(!l && r) return r;
    else if(!l && !r) return NULL;
    else return root;
}
