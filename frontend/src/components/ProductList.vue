<template>
    <div>
        <h1>Product List</h1>
        <ul>
            <li v-for="product in products" :key="product.id">{{ product.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ProductList',
    data() {
        return {
            products: [],
            url: 'https://localhost:8000/'
        };
    },
    created() {
        this.fetchProducts();
    },
    methods: {
        async fetchProducts() {
            try {
                const response = await axios.get(this.url + 'products');
                this.products = response.data;
                console.log('Products:', this.products);
            } catch (error) {
                console.error('Error fetching products:', error);
            }
        }
    }
};
</script>

<style scoped>
/* Add your styles here */
</style>