<template>
  <div>
    <h1>Social Media Downloader</h1>
    <form @submit.prevent="handleSubmit">
      <label for="platform">Select Platform:</label>
      <select v-model="platform" id="platform">
        <option value="tiktok">TikTok</option>
        <option value="instagram">Instagram</option>
        <option value="youtube">YouTube</option>
      </select>

      <label for="link">Paste Link:</label>
      <input type="text" v-model="link" id="link" placeholder="Enter the URL" />

      <button type="submit">Submit</button>
    </form>
    <div v-if="submitted">
      <p>Selected Platform: {{ platform }}</p>
      <p>Link: {{ link }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      platform: 'tiktok',
      link: '',
      submitted: false
    };
  },
  methods: {
    handleSubmit() {
      console.log('Platform:', this.platform);
      console.log('Link:', this.link);
      this.submitted = true;
    }
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

button {
  width: 100px;
}
</style>
