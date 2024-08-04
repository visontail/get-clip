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
    DownloaderForm,
  },
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
  margin: 0;
}
</style>
