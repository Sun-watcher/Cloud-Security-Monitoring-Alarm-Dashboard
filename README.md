# S3 Bucket Visibility Monitoring

## Introduction

Le but de ce projet est de **surveiller les modifications de visibilité d’un bucket S3** et de déclencher des alertes en temps réel lorsqu’un changement est détecté.  

L’objectif est de renforcer la sécurité et la gouvernance des données en garantissant que tout changement d’accès non autorisé soit immédiatement signalé.

---

## Architecture

Le projet repose sur les services AWS suivants :  

1. **CloudTrail**  
   - Enregistre tous les événements liés au bucket S3.  
   - Permet de garder une trace complète des modifications pour l’audit et l’analyse.

2. **CloudWatch**  
   - Surveille les événements CloudTrail spécifiques aux modifications de visibilité.  
   - Crée des métriques et déclenche des alarmes lorsqu’une modification est détectée.  
   - Affiche les alertes dans un **dashboard centralisé** pour une visibilité en temps réel.

3. **Lambda**  
   - Fonction déclenchée par l’alarme CloudWatch.  
   - Envoie un **email de notification** pour informer l’administrateur ou l’équipe de sécurité du changement.

---

## Fonctionnement

1. Un utilisateur modifie la politique d’accès d’un bucket S3.  
2. CloudTrail enregistre cet événement.  
3. CloudWatch analyse les logs CloudTrail et déclenche une alarme si la modification correspond aux critères définis.  
4. La fonction Lambda est exécutée pour envoyer un mail de notification.  
5. L’événement reste consigné dans les logs CloudTrail pour un suivi futur.

---

## Avantages

- **Surveillance en temps réel** des changements de visibilité.  
- **Notifications automatiques** par email pour réagir rapidement.  
- **Traçabilité complète** via CloudTrail pour audit et conformité.  
- **Tableau de bord centralisé** pour une vue globale des événements critiques.

---

## Schéma simplifié

