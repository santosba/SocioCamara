<template>
    <div>
       <h1>Product List</h1>
        <ul>
            <li v-for="product in products" :key="product.id">
                <strong>{{ product.name }}</strong>
                <div v-if="product.price">Price: {{ product.price }}</div>
                <p v-if="product.description">{{ product.description }}</p>
            </li>
        </ul>
        <p v-if="!products.length">No products found.</p>
    </div>
</template>

<script>
import axios from 'axios';
const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/'
});
export default {
    name: 'ProductList',
    data() {
        return {
            products: [],
        
        };
    },
    created() {
        this.fetchProducts();
    },
    methods: {
        async fetchProducts() {
            try {
                const response = await api.get(); // baseURL usada
                // suporta JSON:API (data) ou lista direta
                const payload = response.data && (response.data.data || response.data);
                this.products = Array.isArray(payload) ? payload : (payload.results || []);
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