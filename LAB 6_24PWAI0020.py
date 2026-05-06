import numpy as np

print("\n Task 1: Creating Arrays ")
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3 = np.zeros((4,4))
arr4 = np.ones((2,5))

print(arr1)
print(arr2)
print(arr3)
print(arr4)


print("\n  Task 2: Array Properties")
a = np.array([[1,2,3],[4,5,6]])
print("Shape:", a.shape)
print("Total elements:", a.size)
print("Datatype:", a.dtype)
print("Dimensions:", a.ndim)


print("\n Task 3: Indexing ")
arr = np.array([10,20,30,40,50,60])
print("First:", arr[0])
print("Last:", arr[-1])
print("Third:", arr[2])
print("Greater than 30:", arr[arr > 30])


print("\n Task 4: Slicing")
print(arr[1:5])
print(arr[::-1])
print(arr[::2])

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("First row:", mat[0])
print("Second column:", mat[:,1])
print("Last two rows:", mat[1:])


print("\nTask 5: Vectorization")
v = np.array([1,2,3,4,5])
print(v * 5)
print(v + 10)
print(v ** 2)


print("\n Task 6: Broadcasting")
b = np.array([[1,2,3],[4,5,6]])
print(b + 10)
print(b * 2)


print("\n Task 7: Matrix Add/Subtract")
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])
print("Addition:\n", m1 + m2)
print("Subtraction:\n", m1 - m2)


print("\n Task 8: Matrix Multiplication")
print("Multiplication:\n", np.dot(m1,m2))
print("Transpose:\n", m1.T)


print("\nTask 9: Random Arrays")
rand_arr = np.random.randint(1,101,(4,4))
print(rand_arr)
print("Max:", rand_arr.max())
print("Min:", rand_arr.min())
print("Average:", rand_arr.mean())

dec = np.random.rand(3,3)
print("Random decimals:\n", dec)


print("\n Task 10: Student Marks")
marks = np.array([45,78,82,90,67,88,92,55,49,73])
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Above 80:", len(marks[marks > 80]))
print("Failed:", marks[marks < 50])


print("\n Task 11: Image Pixels")
img = np.random.randint(0,256,(5,5))
print(img)
print("Brightest:", img.max())
print("Darkest:", img.min())
print("Shape:", img.shape)


print("\n Task 12: Normalization")
data = np.array([10,20,30,40,50])
norm = (data - data.min()) / (data.max() - data.min())
print(norm)


print("\n Task 13: Mini Dataset")
dataset = np.array([
    [25,50000,1],
    [30,60000,0],
    [35,80000,1],
    [22,20000,0]
])

X = dataset[:,:2]
y = dataset[:,2]

print("Average salary:", X[:,1].mean())
print("Highest age:", X[:,0].max())
print("Shape:", dataset.shape)