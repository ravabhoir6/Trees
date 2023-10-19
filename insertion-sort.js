class InsertionSort {
    #array = []

    constructor(array) {
        this.#array = array
    }
    
    sort(){

        for(let i=0; i<this.#array.length; i++) {
            let j=i;
            while(j>0 && this.#array[j]<this.#array[j-1]) {
                [this.#array[j], this.#array[j-1]] = [this.#array[j-1], this.#array[j]];
                j--;
            }
        }
        return this.#array;
    }
}

let insertionSort = new InsertionSort([1,6,4,8,3,0, 8, -2]);
console.log(insertionSort.sort())