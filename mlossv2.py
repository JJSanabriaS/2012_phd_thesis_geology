from sklearn.neural_network import MLPClassifier
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
a=clf.fit(X, y)
print(a)
clf.predict([[2., 2.], [-1., -2.]])
[coef.shape for coef in clf.coefs_]
res=clf.predict_proba([[2., 2.], [1., 2.]])
print(res)
