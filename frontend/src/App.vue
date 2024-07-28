<template>
  <div id="app">
    <DownloaderForm />
  </div>
</template>

<script>
import DownloaderForm from './components/DownloaderForm.vue';

export default {
  name: 'App',
  components: {
    DownloaderForm
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
