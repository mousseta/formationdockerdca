# =============================================================================
# DCA PRACTICE SIMULATOR - PARTIE 1 : BASE DE DONNÉES DES QUESTIONS
# =============================================================================
# Ce fichier contient uniquement les données (questions MCQ et DOMC).
# Pour ajouter des questions, il suffit d'éditer ce fichier sans toucher au moteur.
# Format MCQ  : {"id": int, "q": str, "opts": [str, ...], "ans": str, "explanation": str}
# Format DOMC : {"id": int, "q": str, "opts": [(str, bool), ...]}
# =============================================================================

MCQ_QUESTIONS = [

    # -------------------------------------------------------------------------
    # SECTION 1 : Docker Swarm
    # -------------------------------------------------------------------------
    {
        "id": 1,
        "section": "Swarm",
        "q": "Which command initializes a Docker Swarm cluster on the current node?",
        "opts": ["A. docker swarm create", "B. docker swarm init", "C. docker cluster init", "D. docker node init"],
        "ans": "B",
        "explanation": "'docker swarm init' initializes the current node as a Swarm manager."
    },
    {
        "id": 2,
        "section": "Swarm",
        "q": "Which command displays the command needed for a worker node to join an existing Swarm?",
        "opts": ["A. docker swarm token worker", "B. docker swarm join-token worker", "C. docker node token worker", "D. docker service token worker"],
        "ans": "B",
        "explanation": "'docker swarm join-token worker' prints the join command with token for worker nodes."
    },
    {
        "id": 3,
        "section": "Swarm",
        "q": "In Docker Swarm, which node type maintains the cluster state and schedules services?",
        "opts": ["A. Worker", "B. Registry", "C. Manager", "D. Client"],
        "ans": "C",
        "explanation": "Manager nodes maintain cluster state via Raft consensus and schedule tasks."
    },
    {
        "id": 4,
        "section": "Swarm",
        "q": "Which command lists the nodes in a Docker Swarm cluster?",
        "opts": ["A. docker ps", "B. docker node ls", "C. docker swarm ls", "D. docker service ls"],
        "ans": "B",
        "explanation": "'docker node ls' lists all nodes in the Swarm (must be run on a manager)."
    },
    {
        "id": 5,
        "section": "Swarm",
        "q": "Which command creates a service named web with 3 replicas using nginx?",
        "opts": [
            "A. docker run --name web --replicas 3 nginx",
            "B. docker service create --name web --replicas 3 nginx",
            "C. docker swarm service web --replicas 3 nginx",
            "D. docker create service web 3 nginx"
        ],
        "ans": "B",
        "explanation": "'docker service create' is the correct command to create Swarm services."
    },
    {
        "id": 6,
        "section": "Swarm",
        "q": "In Docker Swarm, a service is made up of:",
        "opts": ["A. Volumes only", "B. Images only", "C. One or more tasks", "D. Exactly one container"],
        "ans": "C",
        "explanation": "A service is composed of one or more tasks, each running a container."
    },
    {
        "id": 7,
        "section": "Swarm",
        "q": "Which command shows the tasks associated with a service named api?",
        "opts": ["A. docker service ps api", "B. docker ps service api", "C. docker task ls api", "D. docker swarm ps api"],
        "ans": "A",
        "explanation": "'docker service ps <service>' lists the tasks (and their state) for a service."
    },
    {
        "id": 8,
        "section": "Swarm",
        "q": "Which command changes replicas of an existing service named web to 5?",
        "opts": ["A. docker service scale web=5", "B. docker scale service web 5", "C. docker node scale web=5", "D. docker swarm scale web 5"],
        "ans": "A",
        "explanation": "'docker service scale web=5' is the shorthand to scale a service."
    },
    {
        "id": 9,
        "section": "Swarm",
        "q": "What happens if a container belonging to a Swarm service fails?",
        "opts": [
            "A. Docker Swarm ignores the failure",
            "B. Swarm creates a replacement task to maintain desired state",
            "C. The service is deleted",
            "D. All nodes are restarted"
        ],
        "ans": "B",
        "explanation": "Swarm continuously reconciles actual state with desired state, replacing failed tasks."
    },
    {
        "id": 10,
        "section": "Swarm",
        "q": "Which option publishes container port 80 on cluster port 8080 for a service?",
        "opts": ["A. --port 8080:80", "B. --publish 8080:80", "C. --expose 8080:80", "D. --bind 8080:80"],
        "ans": "B",
        "explanation": "'--publish published=8080,target=80' or '--publish 8080:80' exposes the port via routing mesh."
    },
    {
        "id": 11,
        "section": "Swarm",
        "q": "In Docker Swarm, which network driver is used for communication across nodes?",
        "opts": ["A. bridge", "B. host", "C. overlay", "D. none"],
        "ans": "C",
        "explanation": "Overlay networks span multiple Docker hosts and are used for Swarm inter-node communication."
    },
    {
        "id": 12,
        "section": "Swarm",
        "q": "Which command removes a service named web?",
        "opts": ["A. docker service delete web", "B. docker service rm web", "C. docker rm service web", "D. docker swarm remove web"],
        "ans": "B",
        "explanation": "'docker service rm' removes a service and all its tasks."
    },
    {
        "id": 13,
        "section": "Swarm",
        "q": "Which command updates the image used by a service named web to nginx:1.25?",
        "opts": [
            "A. docker service update --image nginx:1.25 web",
            "B. docker update service --image nginx:1.25 web",
            "C. docker service set-image web nginx:1.25",
            "D. docker swarm update web nginx:1.25"
        ],
        "ans": "A",
        "explanation": "'docker service update --image' performs a rolling update of the service image."
    },
    {
        "id": 14,
        "section": "Swarm",
        "q": "What is the purpose of the Swarm routing mesh?",
        "opts": [
            "A. To encrypt Docker images",
            "B. To route requests to available service tasks regardless of node",
            "C. To create Docker volumes automatically",
            "D. To remove failed nodes"
        ],
        "ans": "B",
        "explanation": "The routing mesh allows any Swarm node to accept connections for published ports and route to available tasks."
    },

    # -------------------------------------------------------------------------
    # SECTION 2 : Image Creation
    # -------------------------------------------------------------------------
    {
        "id": 15,
        "section": "Image Creation",
        "q": "Which command lists the Docker images stored locally on a host?",
        "opts": ["A. docker container ls", "B. docker image ls", "C. docker registry ls", "D. docker volume ls"],
        "ans": "B",
        "explanation": "'docker image ls' (or 'docker images') lists all locally stored images."
    },
    {
        "id": 16,
        "section": "Image Creation",
        "q": "Which command builds an image from a Dockerfile in the current directory?",
        "opts": ["A. docker image create -t myapp:1.0 .", "B. docker build -t myapp:1.0 .", "C. docker run -t myapp:1.0 .", "D. docker tag build myapp:1.0 ."],
        "ans": "B",
        "explanation": "'docker build -t <name:tag> <context>' builds an image from a Dockerfile."
    },
    {
        "id": 17,
        "section": "Image Creation",
        "q": "In a Dockerfile, which instruction specifies the base image?",
        "opts": ["A. BASE", "B. IMAGE", "C. FROM", "D. START"],
        "ans": "C",
        "explanation": "FROM sets the base image for subsequent instructions in the Dockerfile."
    },
    {
        "id": 18,
        "section": "Image Creation",
        "q": "What is the purpose of the .dockerignore file?",
        "opts": [
            "A. To ignore running containers",
            "B. To exclude files from the build context",
            "C. To prevent pushing images",
            "D. To hide instructions"
        ],
        "ans": "B",
        "explanation": ".dockerignore excludes files/directories from the build context sent to the daemon, reducing build time and image size."
    },
    {
        "id": 19,
        "section": "Image Creation",
        "q": "Which Dockerfile instruction executes commands at image build time?",
        "opts": ["A. CMD", "B. RUN", "C. ENTRYPOINT", "D. EXEC"],
        "ans": "B",
        "explanation": "RUN executes commands in a new layer during build. CMD and ENTRYPOINT define runtime behavior."
    },
    {
        "id": 20,
        "section": "Image Creation",
        "q": "Which Dockerfile instruction defines the default command for a container start?",
        "opts": ["A. RUN", "B. COPY", "C. CMD", "D. BUILD"],
        "ans": "C",
        "explanation": "CMD provides defaults for container execution. It can be overridden at runtime."
    },
    {
        "id": 21,
        "section": "Image Creation",
        "q": "Which command tags a local image for a repository?",
        "opts": [
            "A. docker image tag myapp:1.0 john/myapp:1.0",
            "B. docker push myapp:1.0 john/myapp:1.0",
            "C. docker rename myapp:1.0 john/myapp:1.0",
            "D. docker build tag john/myapp:1.0"
        ],
        "ans": "A",
        "explanation": "'docker image tag SOURCE TARGET' creates a new tag for an existing image."
    },
    {
        "id": 22,
        "section": "Image Creation",
        "q": "Which command uploads an image to a registry?",
        "opts": ["A. docker upload", "B. docker image send", "C. docker push", "D. docker registry push"],
        "ans": "C",
        "explanation": "'docker push <image>' uploads the image layers to a registry."
    },
    {
        "id": 23,
        "section": "Image Creation",
        "q": "Which command downloads an image from a registry without running it?",
        "opts": ["A. docker get", "B. docker pull", "C. docker fetch", "D. docker image download"],
        "ans": "B",
        "explanation": "'docker pull' downloads image layers from a registry without creating a container."
    },
    {
        "id": 24,
        "section": "Image Creation",
        "q": "Which command displays detailed metadata about a Docker image?",
        "opts": [
            "A. docker image inspect <image>",
            "B. docker image metadata <image>",
            "C. docker image describe <image>",
            "D. docker show image <image>"
        ],
        "ans": "A",
        "explanation": "'docker image inspect' returns detailed JSON metadata about an image."
    },
    {
        "id": 25,
        "section": "Image Creation",
        "q": "What is the main difference between CMD and ENTRYPOINT?",
        "opts": [
            "A. CMD runs at build time",
            "B. ENTRYPOINT defines executable, CMD provides arguments",
            "C. ENTRYPOINT only for Windows",
            "D. CMD cannot be overridden"
        ],
        "ans": "B",
        "explanation": "ENTRYPOINT sets the fixed executable; CMD sets default arguments. CMD can be easily overridden at runtime."
    },

    # -------------------------------------------------------------------------
    # SECTION 3 : Installation & Configuration
    # -------------------------------------------------------------------------
    {
        "id": 26,
        "section": "Installation & Configuration",
        "q": "Which command shows Docker version for client and server?",
        "opts": ["A. docker info", "B. docker version", "C. docker system version", "D. docker engine version"],
        "ans": "B",
        "explanation": "'docker version' shows version details for both the client and the Docker daemon."
    },
    {
        "id": 27,
        "section": "Installation & Configuration",
        "q": "Which command displays system-wide Docker information?",
        "opts": ["A. docker system inspect", "B. docker version", "C. docker info", "D. docker config ls"],
        "ans": "C",
        "explanation": "'docker info' displays system-wide info: containers, images, storage driver, plugins, etc."
    },
    {
        "id": 28,
        "section": "Installation & Configuration",
        "q": "On systemd Linux, which command starts Docker?",
        "opts": ["A. systemctl start docker", "B. docker daemon start", "C. service docker enable", "D. docker start daemon"],
        "ans": "A",
        "explanation": "On systemd-based Linux distributions, 'systemctl start docker' starts the Docker service."
    },
    {
        "id": 29,
        "section": "Installation & Configuration",
        "q": "Which command enables Docker to start at boot?",
        "opts": ["A. docker enable", "B. systemctl enable docker", "C. docker system enable", "D. systemctl boot docker"],
        "ans": "B",
        "explanation": "'systemctl enable docker' configures Docker to start automatically on system boot."
    },
    {
        "id": 30,
        "section": "Installation & Configuration",
        "q": "Which file configures Docker daemon options on Linux?",
        "opts": [
            "A. /etc/docker/daemon.json",
            "B. /var/lib/docker/config.json",
            "C. /etc/docker/client.json",
            "D. /usr/bin/docker.json"
        ],
        "ans": "A",
        "explanation": "/etc/docker/daemon.json is the standard location for Docker daemon configuration on Linux."
    },
    {
        "id": 31,
        "section": "Installation & Configuration",
        "q": "What is required after modifying daemon configuration?",
        "opts": ["A. Rebuild images", "B. Restart Docker daemon", "C. Remove containers", "D. Logout"],
        "ans": "B",
        "explanation": "Changes to daemon.json require a daemon restart: 'systemctl restart docker'."
    },
    {
        "id": 32,
        "section": "Installation & Configuration",
        "q": "Which command shows disk usage for Docker objects?",
        "opts": ["A. docker system df", "B. docker disk ls", "C. docker storage show", "D. docker image usage"],
        "ans": "A",
        "explanation": "'docker system df' shows disk usage for images, containers, volumes, and build cache."
    },
    {
        "id": 33,
        "section": "Installation & Configuration",
        "q": "Which command removes unused Docker data (prune)?",
        "opts": ["A. docker clean all", "B. docker system prune", "C. docker remove unused", "D. docker daemon prune"],
        "ans": "B",
        "explanation": "'docker system prune' removes stopped containers, unused networks, dangling images, and build cache."
    },

    # -------------------------------------------------------------------------
    # SECTION 4 : Networking
    # -------------------------------------------------------------------------
    {
        "id": 34,
        "section": "Networking",
        "q": "Which command lists Docker networks?",
        "opts": ["A. docker network ls", "B. docker net show", "C. docker network inspect", "D. docker container network"],
        "ans": "A",
        "explanation": "'docker network ls' lists all networks available on the Docker host."
    },
    {
        "id": 35,
        "section": "Networking",
        "q": "Default network driver for standalone containers?",
        "opts": ["A. overlay", "B. bridge", "C. host", "D. macvlan"],
        "ans": "B",
        "explanation": "The default network for standalone containers is 'bridge', creating an internal private network."
    },
    {
        "id": 36,
        "section": "Networking",
        "q": "Which command creates a user-defined bridge network?",
        "opts": [
            "A. docker network create appnet",
            "B. docker bridge create appnet",
            "C. docker network add appnet",
            "D. docker create network bridge"
        ],
        "ans": "A",
        "explanation": "'docker network create' creates a user-defined network (bridge by default)."
    },
    {
        "id": 37,
        "section": "Networking",
        "q": "Connect container web to network appnet?",
        "opts": [
            "A. docker network attach appnet web",
            "B. docker container connect web appnet",
            "C. docker network connect appnet web",
            "D. docker connect network appnet web"
        ],
        "ans": "C",
        "explanation": "'docker network connect <network> <container>' connects a running container to a network."
    },
    {
        "id": 38,
        "section": "Networking",
        "q": "Disconnect container web from appnet?",
        "opts": [
            "A. docker network disconnect appnet web",
            "B. docker network remove appnet web",
            "C. docker disconnect network web appnet",
            "D. docker container disconnect web appnet"
        ],
        "ans": "A",
        "explanation": "'docker network disconnect <network> <container>' removes a container from a network."
    },
    {
        "id": 39,
        "section": "Networking",
        "q": "What does the host network driver do?",
        "opts": ["A. Isolated namespace", "B. Disables networking", "C. Shares host network namespace", "D. Overlay network"],
        "ans": "C",
        "explanation": "With 'host' driver, the container shares the host's network namespace — no isolation, no NAT."
    },
    {
        "id": 40,
        "section": "Networking",
        "q": "Publish port 80 on host port 8080?",
        "opts": [
            "A. docker run --expose 8080:80",
            "B. docker run -p 8080:80",
            "C. docker run --network 8080:80",
            "D. docker run --port 80:8080"
        ],
        "ans": "B",
        "explanation": "'-p host_port:container_port' maps a host port to a container port."
    },
    {
        "id": 41,
        "section": "Networking",
        "q": "Network driver for multi-host Swarm?",
        "opts": ["A. bridge", "B. host", "C. overlay", "D. none"],
        "ans": "C",
        "explanation": "Overlay networks span multiple Docker hosts, essential for Swarm service communication."
    },

    # -------------------------------------------------------------------------
    # SECTION 5 : Security
    # -------------------------------------------------------------------------
    {
        "id": 42,
        "section": "Security",
        "q": "Run container with read-only root filesystem?",
        "opts": ["A. docker run --readonly", "B. docker run --read-only", "C. docker run --rootfs", "D. docker run --secure"],
        "ans": "B",
        "explanation": "'--read-only' mounts the container's root filesystem as read-only, preventing runtime modifications."
    },
    {
        "id": 43,
        "section": "Security",
        "q": "Run container as UID 1000?",
        "opts": ["A. docker run --uid 1000", "B. docker run --user 1000", "C. docker run --run-as 1000", "D. docker run --security"],
        "ans": "B",
        "explanation": "'--user <uid>' sets the user/UID the container process runs as."
    },
    {
        "id": 44,
        "section": "Security",
        "q": "Dockerfile instruction for default user?",
        "opts": ["A. RUNUSER", "B. SETUSER", "C. USER", "D. DEFAULTUSER"],
        "ans": "C",
        "explanation": "The USER instruction sets the username or UID for subsequent RUN, CMD, and ENTRYPOINT instructions."
    },
    {
        "id": 45,
        "section": "Security",
        "q": "Add Linux capability to a container?",
        "opts": ["A. --add-cap", "B. --cap-add", "C. --capability-add", "D. --linux-cap"],
        "ans": "B",
        "explanation": "'--cap-add <capability>' grants a specific Linux capability to the container."
    },
    {
        "id": 46,
        "section": "Security",
        "q": "Remove Linux capability from a container?",
        "opts": ["A. --cap-remove", "B. --cap-drop", "C. --drop-capability", "D. --remove-cap"],
        "ans": "B",
        "explanation": "'--cap-drop <capability>' removes a specific Linux capability, following least-privilege principle."
    },
    {
        "id": 47,
        "section": "Security",
        "q": "Purpose of Docker Content Trust?",
        "opts": [
            "A. Encrypt volumes",
            "B. Verify integrity and authenticity of images (signing)",
            "C. Scan open ports",
            "D. Isolate hosts"
        ],
        "ans": "B",
        "explanation": "Docker Content Trust (DCT) uses digital signatures to verify image publisher identity and integrity."
    },
    {
        "id": 48,
        "section": "Security",
        "q": "Environment variable to enable Docker Content Trust?",
        "opts": ["A. DOCKER_TRUST=1", "B. DOCKER_CONTENT_TRUST=1", "C. DOCKER_SIGNED=1", "D. DOCKER_SECURITY=enabled"],
        "ans": "B",
        "explanation": "Setting DOCKER_CONTENT_TRUST=1 enables DCT for all push/pull/run operations."
    },
    {
        "id": 49,
        "section": "Security",
        "q": "Limit container memory to 256 MB?",
        "opts": ["A. docker run --memory 256m", "B. docker run --mem-limit 256m", "C. docker run --limit-ram", "D. docker run --max-ram"],
        "ans": "A",
        "explanation": "'--memory 256m' sets a hard memory limit. Combined with --memory-swap for swap control."
    },

    # -------------------------------------------------------------------------
    # SECTION 6 : Storage
    # -------------------------------------------------------------------------
    {
        "id": 50,
        "section": "Storage",
        "q": "Create named volume appdata?",
        "opts": ["A. docker storage create", "B. docker volume create appdata", "C. docker create volume", "D. docker data create"],
        "ans": "B",
        "explanation": "'docker volume create <name>' creates a named volume managed by Docker."
    },
    {
        "id": 51,
        "section": "Storage",
        "q": "List Docker volumes?",
        "opts": ["A. docker volume ls", "B. docker storage ls", "C. docker data ls", "D. docker mount ls"],
        "ans": "A",
        "explanation": "'docker volume ls' lists all volumes on the Docker host."
    },
    {
        "id": 52,
        "section": "Storage",
        "q": "Mount volume webdata to /usr/share/nginx/html?",
        "opts": [
            "A. docker run -v webdata:/usr/share/nginx/html",
            "B. docker run -v /usr/share/nginx/html:webdata",
            "C. docker run --volume path:name",
            "D. docker run --mount webdata"
        ],
        "ans": "A",
        "explanation": "'-v volume_name:container_path' mounts a named volume. Order is source:destination."
    },
    {
        "id": 53,
        "section": "Storage",
        "q": "Main purpose of Docker volumes?",
        "opts": [
            "A. Persistent data outside container lifecycle",
            "B. Reduce image size",
            "C. Publish ports",
            "D. Encrypt networks"
        ],
        "ans": "A",
        "explanation": "Volumes persist data independently of the container lifecycle and can be shared between containers."
    },
    {
        "id": 54,
        "section": "Storage",
        "q": "Detailed information about a volume?",
        "opts": [
            "A. docker volume describe",
            "B. docker volume inspect appdata",
            "C. docker inspect volume",
            "D. docker storage inspect"
        ],
        "ans": "B",
        "explanation": "'docker volume inspect <name>' returns JSON metadata including mount point and driver."
    },
    {
        "id": 55,
        "section": "Storage",
        "q": "Remove unused volumes?",
        "opts": ["A. docker volume clean", "B. docker volume prune", "C. docker prune volumes", "D. docker storage prune"],
        "ans": "B",
        "explanation": "'docker volume prune' removes all volumes not used by at least one container."
    },
]

# =============================================================================
# QUESTIONS DOMC (Discrete Option Multiple Choice)
# Chaque option est un tuple (statement: str, is_correct: bool)
# =============================================================================

DOMC_QUESTIONS = [
    {
        "id": 1,
        "section": "Swarm",
        "q": "Which command initializes a Docker Swarm cluster?",
        "opts": [
            ("docker swarm init", True),
            ("docker swarm create", False),
            ("docker node init", False),
            ("docker cluster init", False)
        ]
    },
    {
        "id": 2,
        "section": "Swarm",
        "q": "Which command displays join command for worker node?",
        "opts": [
            ("docker swarm join-token worker", True),
            ("docker node join-token worker", False),
            ("docker swarm token worker", False),
            ("docker service join worker", False)
        ]
    },
    {
        "id": 3,
        "section": "Swarm",
        "q": "Correct statements about Swarm managers:",
        "opts": [
            ("Maintain cluster state", True),
            ("Participate in Raft consensus", True),
            ("Cannot run service tasks", False),
            ("Responsible for scheduling", True)
        ]
    },
    {
        "id": 4,
        "section": "Swarm",
        "q": "List all nodes in Swarm:",
        "opts": [
            ("docker node ls", True),
            ("docker swarm ls", False),
            ("docker nodes", False),
            ("docker cluster nodes", False)
        ]
    },
    {
        "id": 5,
        "section": "Swarm",
        "q": "Valid commands to manage replicated services:",
        "opts": [
            ("docker service create --replicas 3", True),
            ("docker run --replicas 3", False),
            ("docker service scale", True),
            ("docker service update --replicas", True)
        ]
    },
    {
        "id": 6,
        "section": "Swarm",
        "q": "True statements about containers vs services:",
        "opts": [
            ("Container is a running instance", True),
            ("Service defines desired state", True),
            ("Service can only run one container", False),
            ("Swarm keeps service in desired state", True)
        ]
    },
    {
        "id": 7,
        "section": "Swarm",
        "q": "Commands to display service tasks:",
        "opts": [
            ("docker service ps api", True),
            ("docker task ls api", False),
            ("docker service tasks api", False),
            ("docker ps --service api", False)
        ]
    },
    {
        "id": 8,
        "section": "Swarm",
        "q": "True statements about Swarm desired state:",
        "opts": [
            ("Swarm replaces failed tasks", True),
            ("Failed container deletes service", False),
            ("Swarm compares actual vs desired state", True),
            ("Desired state only for standalone containers", False)
        ]
    },
    {
        "id": 9,
        "section": "Swarm",
        "q": "Valid commands to update or remove a Swarm service:",
        "opts": [
            ("docker service update --image", True),
            ("docker service rm", True),
            ("docker rm service", False),
            ("docker service set-image", False)
        ]
    },
    {
        "id": 10,
        "section": "Swarm",
        "q": "True statements about global services:",
        "opts": [
            ("Run one task on every node", True),
            ("Created with --mode global", True),
            ("Requires a fixed replica count", False),
            ("Useful for monitoring agents", True)
        ]
    },
    {
        "id": 11,
        "section": "Swarm",
        "q": "Valid commands to manage node availability:",
        "opts": [
            ("docker node update --availability drain", True),
            ("docker node update --availability active", True),
            ("docker node drain node1", False),
            ("docker service drain", False)
        ]
    },
    {
        "id": 12,
        "section": "Swarm",
        "q": "True statements about quorum in Swarm:",
        "opts": [
            ("Uses Raft consensus algorithm", True),
            ("Majority of managers required for quorum", True),
            ("Losing quorum has no effect on cluster", False),
            ("Odd number of managers recommended", True)
        ]
    },
    {
        "id": 13,
        "section": "Swarm",
        "q": "True statements about node labels and constraints:",
        "opts": [
            ("docker node update --label-add", True),
            ("docker service create --constraint", True),
            ("docker service create --node-label", False),
            ("Labels can control task scheduling", True)
        ]
    },
    {
        "id": 14,
        "section": "Swarm",
        "q": "Valid commands to manage Docker stacks:",
        "opts": [
            ("docker stack deploy -c file.yml", True),
            ("docker stack ls", True),
            ("docker stack services app", True),
            ("docker compose stack deploy", False)
        ]
    },
]
