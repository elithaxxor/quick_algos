def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    print(products)

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
                print(runningProduct)
                products[i] = runningProduct
        return products


def arrayOfProductsii(array):
    products = [1 for _ in range(len(array))]

    rightRunningProduct = 1
    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    for i in range(len(array)):
        products[i] = rightRunningProduct
        rightRunningProduct*= array[i]

    return products

array = [5, 1, 4, 2]
result = arrayOfProductsii(array)
print(result)





    