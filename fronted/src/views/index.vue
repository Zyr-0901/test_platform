<template>
    <v-app id="inspire">
        <!-- 侧边栏 -->
        <v-navigation-drawer v-model="drawer" app>
            <!--  -->
        </v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title>Application</v-toolbar-title>
        </v-app-bar>

        <!-- 主体内容 -->
        <v-main>
            <!--  -->
        </v-main>
    </v-app>
</template>

<script>
export default {
    data: () => ({ drawer: null }),
}
</script>