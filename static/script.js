document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // If clicking "Start Free Trial", focus on the username input
                if (targetId === '#start') {
                    setTimeout(() => {
                        document.getElementById('username').focus();
                    }, 800);
                }
            }
        });
    });

    // After the logo animation completes, show the main container
    setTimeout(() => {
        document.querySelector('.main-container').style.display = 'block';
    }, 2500);

    const searchBtn = document.getElementById('searchBtn');
    const usernameInput = document.getElementById('username');
    const resultsDiv = document.getElementById('results');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error');
    const foundCountSpan = document.getElementById('foundCount');
    const totalCheckedSpan = document.getElementById('totalChecked');
    const searchedUsernameSpan = document.getElementById('searchedUsername');

    searchBtn.addEventListener('click', function() {
        const username = usernameInput.value.trim();
        if (!username) {
            showError('Please enter a username');
            return;
        }

        // Clear previous results and show loading
        resultsDiv.style.display = 'none';
        errorDiv.style.display = 'none';
        loadingDiv.style.display = 'block';

        // Make the API request
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}`
        })
        .then(response => response.json())
        .then(data => {
            loadingDiv.style.display = 'none';
            
            if (data.error) {
                showError(data.error);
                return;
            }

            // Update stats
            foundCountSpan.textContent = data.found_count;
            totalCheckedSpan.textContent = data.total_checked;
            searchedUsernameSpan.textContent = data.username;

            // Clear previous results
            document.querySelectorAll('.platform-list').forEach(list => list.innerHTML = '');

            // Process results by category
            processPlatforms(data.platforms, data.categories.important, 'importantPlatforms');
            processPlatforms(data.platforms, data.categories.secondary, 'secondaryPlatforms');
            processPlatforms(data.platforms, data.categories.other, 'otherPlatforms');

            // Show results with animation
            resultsDiv.style.display = 'block';
            resultsDiv.style.opacity = '0';
            setTimeout(() => {
                resultsDiv.style.opacity = '1';
            }, 100);
        })
        .catch(error => {
            loadingDiv.style.display = 'none';
            showError('An error occurred while searching. Please try again.');
            console.error('Error:', error);
        });
    });

    function processPlatforms(platforms, platformList, containerId) {
        const container = document.getElementById(containerId).querySelector('.platform-list');
        
        platformList.forEach(platform => {
            const result = platforms[platform];
            if (!result) return;

            const platformItem = document.createElement('div');
            platformItem.className = 'platform-item';
            
            platformItem.innerHTML = `
                <div class="platform-link">
                    <div class="platform-icon">
                        <i class="fab fa-${platform}"></i>
                    </div>
                    <div class="platform-name">${platform.charAt(0).toUpperCase() + platform.slice(1)}</div>
                    <div class="platform-status">
                        <a href="${result.url}" target="_blank" class="btn btn-visit">
                            <i class="fas fa-external-link-alt"></i> Visit
                        </a>
                    </div>
                </div>
            `;

            container.appendChild(platformItem);
        });
    }

    function showError(message) {
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
        errorDiv.style.opacity = '0';
        setTimeout(() => {
            errorDiv.style.opacity = '1';
        }, 100);
    }
}); 