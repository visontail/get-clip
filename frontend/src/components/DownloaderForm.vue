<template>
  <div class="downloader-form">
    <h1>Social Media Downloader</h1>
    <div class="buttons">
      <button
        v-for="option in options"
        :key="option.value"
        @click="selectOption(option.value)"
        :class="{ active: platform === option.value }"
      >
        {{ option.label }}
      </button>
    </div>
    <div v-if="platform" class="link-input">
      <label for="link">Paste Link:</label>
      <input type="text" v-model="link" id="link" placeholder="Enter the URL" />
      <button @click="handleSubmit">Submit</button>
    </div>
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
      options: [
        { label: 'TikTok', value: 'tiktok' },
        { label: 'Instagram', value: 'instagram' },
        { label: 'YouTube', value: 'youtube' },
      ],
      platform: null,
      link: '',
      submitted: false,
    };
  },
  methods: {
    selectOption(platform) {
      this.platform = platform;
      this.link = '';
      this.submitted = false;
    },
    handleSubmit() {
      console.log('Platform:', this.platform);
      console.log('Link:', this.link);
      this.submitted = true;
    },
  },
};
</script>

<style scoped>
.downloader-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

.buttons {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #42b983;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2a8b60;
}

button.active {
  background-color: #1a6140;
}

.link-input {
  margin-bottom: 20px;
}

input[type="text"] {
  padding: 10px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

button {
  padding: 10px 20px;
}
</style>
