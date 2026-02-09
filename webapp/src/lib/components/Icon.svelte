<script>
    import { icons, getIcon, platformColors } from '$lib/icons.js';
    
    export let name = '';
    export let size = 24;
    export let color = 'currentColor';
    export let platform = null; // If set, uses platform color
    
    $: iconSvg = getIcon(name, size);
    $: style = platform ? `color: ${platformColors[platform]}` : (color !== 'currentColor' ? `color: ${color}` : '');
</script>

<span class="icon" {style}>
    {@html iconSvg}
</span>

<style>
    .icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    
    .icon :global(svg) {
        display: block;
    }
</style>
