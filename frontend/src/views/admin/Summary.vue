<template>
    <h2>Admin Summary</h2>

    <div style="width: 50%">
        <canvas id="myChart"></canvas>
    </div>

    <!-- <img src="http://127.0.0.1:5000/static/graphs/image.png" alt=""> -->

</template>

<script>
import Chart from 'chart.js/auto';

export default {
    name: 'AdminDashboard',
    data() {
        return {
            label: null,
            labels: null,
            noOfSpots: null
        }
    },
    methods: {
        fetchData() {
            fetch('http://127.0.0.1:5000/graph')
            .then(response => response.json())
            .then(data => {
                console.log('response from be: ', data)
                this.label = data.label
                this.labels = data.labels
                this.noOfSpots = data.data
                this.generateGraph()
            })
        },
        generateGraph() {
            const ctx = document.getElementById('myChart');
            new Chart(ctx, {
                type: 'bar',
                data: {
                labels: this.labels,
                datasets: [{
                    label: this.label,
                    data: this.noOfSpots,
                    borderWidth: 1
                }]
                },
                options: {
                scales: {
                    y: {
                    beginAtZero: true
                    }
                }
                }
            });
        }
    },
    mounted() { // a fucntion which runs when component is loaded on browser
        
        this.fetchData()

    }
}
</script>