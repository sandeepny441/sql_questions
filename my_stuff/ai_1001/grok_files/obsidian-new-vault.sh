#!/bin/zsh
# =====================================================
# Obsidian New Vault Helper (macOS + zsh)
# Creates a new vault and copies settings from your master vault.
# Excludes workspace.json, graph.json, and selected plugin data folders.
# =====================================================

# === CONFIGURE THIS ===
MASTER_VAULT="/Users/san/Documents/obsidian_vaults/mbs_valut"

# Add the folder names of plugins whose data you want to RESET in new vaults.
# These plugins will be installed, but their saved data will start fresh.
# Common ones people exclude:
#   - "obsidian-git"
#   - "dataview" 
#   - "templater-obsidian"
#   - "obsidian-kanban"
#   - "obsidian-tasks"
#   - "smart-connections"
EXCLUDED_PLUGIN_DATA=(
    # "obsidian-git"
    # "dataview"
    # "templater-obsidian"
)

# =====================================================

new-obsidian-vault() {
    local new_vault_path="$1"

    if [[ -z "$new_vault_path" ]]; then
        echo "Usage: new-obsidian-vault /full/path/to/new-vault-folder"
        echo "Example: new-obsidian-vault ~/Documents/Work/MyNewProject"
        return 1
    fi

    new_vault_path="${new_vault_path/#\~/$HOME}"

    if [[ ! -d "$MASTER_VAULT" ]]; then
        echo "Error: Master vault not found at: $MASTER_VAULT"
        return 1
    fi

    echo "Creating new vault at: $new_vault_path"
    mkdir -p "$new_vault_path"

    local source_config="$MASTER_VAULT/.obsidian"
    local dest_config="$new_vault_path/.obsidian"

    if [[ -d "$dest_config" ]]; then
        echo "A .obsidian folder already exists in the destination."
        read -q "REPLY?Overwrite it? (y/n) "
        echo
        if [[ "$REPLY" != "y" ]]; then
            echo "Cancelled."
            return 1
        fi
        rm -rf "$dest_config"
    fi

    echo "Copying settings (excluding workspace, graph, and selected plugin data)..."
    mkdir -p "$dest_config"

    # Build rsync exclude arguments
    local exclude_args=()
    exclude_args+=(--exclude='workspace.json')
    exclude_args+=(--exclude='graph.json')

    for plugin in "${EXCLUDED_PLUGIN_DATA[@]}"; do
        if [[ -n "$plugin" ]]; then
            exclude_args+=(--exclude="plugins/$plugin/data.json")
            # Some plugins also store other files in their folder
            exclude_args+=(--exclude="plugins/$plugin/*.json")
        fi
    done

    # Copy with exclusions
    rsync -a "${exclude_args[@]}" "$source_config/" "$dest_config/"

    echo ""
    echo "✅ Done!"
    echo "New vault created at: $new_vault_path"
    echo ""
    echo "Next steps:"
    echo "1. Open Obsidian"
    echo "2. File → Open folder as vault"
    echo "3. Select: $new_vault_path"
    echo ""
    echo "Your plugins and themes are copied, but workspace, graph, and selected plugin data are reset."
}

# =====================================================
# How to use:
# 1. Edit MASTER_VAULT path above.
# 2. Add plugin folder names to EXCLUDED_PLUGIN_DATA if desired.
# 3. Add this line to your ~/.zshrc:
#    source /Users/san/Documents/ai_1001/grok_files/obsidian-new-vault.sh
# 4. Reload: source ~/.zshrc
# 5. Use: new-obsidian-vault ~/path/to/new-vault
# =====================================================