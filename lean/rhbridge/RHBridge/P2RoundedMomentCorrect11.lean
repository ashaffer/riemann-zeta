import RHBridge.P2RoundedFlatFactorCheckpoint11
import RHBridge.P2RoundedMomentLengths11
import RHBridge.P2RoundedMomentCheckpointCheck11_moments
import RHBridge.P2RoundedMomentCheckpointCheck11_mode0
import RHBridge.P2RoundedMomentCheckpointCheck11_mode1
import RHBridge.P2RoundedMomentCheckpointCheck11_mode2
import RHBridge.P2RoundedMomentCheckpointCheck11_mode3
import RHBridge.P2RoundedMomentCheckpointCheck11_mode4
import RHBridge.P2RoundedMomentCheckpointCheck11_mode5
import RHBridge.P2RoundedMomentCheckpointCheck11_mode6
import RHBridge.P2RoundedMomentCheckpointCheck11_mode7
import RHBridge.P2RoundedMomentCheckpointCheck11_mode8
import RHBridge.P2RoundedMomentCheckpointCheck11_mode9
import RHBridge.P2RoundedMomentCheckpointCheck11_mode10
import RHBridge.P2RoundedMomentCheckpointCheck11_mode11
import RHBridge.P2RoundedMomentCheckpointCheck11_mode12
import RHBridge.P2RoundedMomentCheckpointCheck11_mode13
import RHBridge.P2RoundedMomentCheckpointCheck11_mode14
import RHBridge.P2RoundedMomentCheckpointCheck11_mode15
import RHBridge.P2RoundedMomentCheckpointCheck11_mode16
import RHBridge.P2RoundedMomentCheckpointCheck11_mode17
import RHBridge.P2RoundedMomentCheckpointCheck11_mode18
import RHBridge.P2RoundedMomentCheckpointCheck11_mode19
import RHBridge.P2RoundedMomentCheckpointCheck11_mode20
import RHBridge.P2RoundedMomentCheckpointCheck11_mode21
import RHBridge.P2RoundedMomentCheckpointCheck11_mode22
import RHBridge.P2RoundedMomentCheckpointCheck11_mode23
import RHBridge.P2RoundedMomentCheckpointCheck11_mode24
import RHBridge.P2RoundedMomentCheckpointCheck11_mode25
import RHBridge.P2RoundedMomentCheckpointCheck11_mode26
import RHBridge.P2RoundedMomentCheckpointCheck11_mode27
import RHBridge.P2RoundedMomentCheckpointCheck11_mode28
import RHBridge.P2RoundedMomentCheckpointCheck11_mode29
import RHBridge.P2RoundedMomentCheckpointCheck11_mode30
import RHBridge.P2RoundedMomentCheckpointCheck11_mode31
import RHBridge.P2RoundedMomentCheckpointCheck11_mode32
import RHBridge.P2RoundedMomentCheckpointCheck11_mode33
import RHBridge.P2RoundedMomentCheckpointCheck11_mode34
import RHBridge.P2RoundedMomentCheckpointCheck11_mode35
import RHBridge.P2RoundedMomentCheckpointCheck11_mode36
import RHBridge.P2RoundedMomentCheckpointCheck11_mode37
import RHBridge.P2RoundedMomentCheckpointCheck11_mode38
import RHBridge.P2RoundedMomentCheckpointCheck11_mode39
import RHBridge.P2RoundedMomentCheckpointCheck11_mode40
import RHBridge.P2RoundedMomentCheckpointCheck11_mode41
import RHBridge.P2RoundedMomentCheckpointCheck11_mode42
import RHBridge.P2RoundedMomentCheckpointCheck11_mode43
import RHBridge.P2RoundedMomentCheckpointCheck11_mode44
import RHBridge.P2RoundedMomentCheckpointCheck11_mode45
import RHBridge.P2RoundedMomentCheckpointCheck11_mode46
import RHBridge.P2RoundedMomentCheckpointCheck11_mode47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedMomentRefinement

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

private theorem vector_ext_fin
    {α : Type} {n : Nat} {v w : Vector α n}
    (h : ∀ i : Fin n, v.get i = w.get i) : v = w := by
  apply Vector.ext
  intro i hi
  exact h ⟨i, hi⟩

theorem panel11DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel11FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11DefectMomentRange0) panel11DefectMomentRange64) panel11DefectMomentRange128) panel11DefectMomentRange192) panel11DefectMomentRange256) row

theorem panel11Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode0MatVecRange0) panel11Mode0MatVecRange32) panel11Mode0MatVecRange64) panel11Mode0MatVecRange96) panel11Mode0MatVecRange128) row

theorem panel11Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode1MatVecRange0) panel11Mode1MatVecRange32) panel11Mode1MatVecRange64) panel11Mode1MatVecRange96) panel11Mode1MatVecRange128) row

theorem panel11Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode2MatVecRange0) panel11Mode2MatVecRange32) panel11Mode2MatVecRange64) panel11Mode2MatVecRange96) panel11Mode2MatVecRange128) row

theorem panel11Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode3MatVecRange0) panel11Mode3MatVecRange32) panel11Mode3MatVecRange64) panel11Mode3MatVecRange96) panel11Mode3MatVecRange128) row

theorem panel11Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode4MatVecRange0) panel11Mode4MatVecRange32) panel11Mode4MatVecRange64) panel11Mode4MatVecRange96) panel11Mode4MatVecRange128) row

theorem panel11Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode5MatVecRange0) panel11Mode5MatVecRange32) panel11Mode5MatVecRange64) panel11Mode5MatVecRange96) panel11Mode5MatVecRange128) row

theorem panel11Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode6MatVecRange0) panel11Mode6MatVecRange32) panel11Mode6MatVecRange64) panel11Mode6MatVecRange96) panel11Mode6MatVecRange128) row

theorem panel11Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode7MatVecRange0) panel11Mode7MatVecRange32) panel11Mode7MatVecRange64) panel11Mode7MatVecRange96) panel11Mode7MatVecRange128) row

theorem panel11Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode8MatVecRange0) panel11Mode8MatVecRange32) panel11Mode8MatVecRange64) panel11Mode8MatVecRange96) panel11Mode8MatVecRange128) row

theorem panel11Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode9MatVecRange0) panel11Mode9MatVecRange32) panel11Mode9MatVecRange64) panel11Mode9MatVecRange96) panel11Mode9MatVecRange128) row

theorem panel11Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode10MatVecRange0) panel11Mode10MatVecRange32) panel11Mode10MatVecRange64) panel11Mode10MatVecRange96) panel11Mode10MatVecRange128) row

theorem panel11Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode11MatVecRange0) panel11Mode11MatVecRange32) panel11Mode11MatVecRange64) panel11Mode11MatVecRange96) panel11Mode11MatVecRange128) row

theorem panel11Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode12MatVecRange0) panel11Mode12MatVecRange32) panel11Mode12MatVecRange64) panel11Mode12MatVecRange96) panel11Mode12MatVecRange128) row

theorem panel11Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode13MatVecRange0) panel11Mode13MatVecRange32) panel11Mode13MatVecRange64) panel11Mode13MatVecRange96) panel11Mode13MatVecRange128) row

theorem panel11Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode14MatVecRange0) panel11Mode14MatVecRange32) panel11Mode14MatVecRange64) panel11Mode14MatVecRange96) panel11Mode14MatVecRange128) row

theorem panel11Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode15MatVecRange0) panel11Mode15MatVecRange32) panel11Mode15MatVecRange64) panel11Mode15MatVecRange96) panel11Mode15MatVecRange128) row

theorem panel11Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode16MatVecRange0) panel11Mode16MatVecRange32) panel11Mode16MatVecRange64) panel11Mode16MatVecRange96) panel11Mode16MatVecRange128) row

theorem panel11Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode17MatVecRange0) panel11Mode17MatVecRange32) panel11Mode17MatVecRange64) panel11Mode17MatVecRange96) panel11Mode17MatVecRange128) row

theorem panel11Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode18MatVecRange0) panel11Mode18MatVecRange32) panel11Mode18MatVecRange64) panel11Mode18MatVecRange96) panel11Mode18MatVecRange128) row

theorem panel11Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode19MatVecRange0) panel11Mode19MatVecRange32) panel11Mode19MatVecRange64) panel11Mode19MatVecRange96) panel11Mode19MatVecRange128) row

theorem panel11Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode20MatVecRange0) panel11Mode20MatVecRange32) panel11Mode20MatVecRange64) panel11Mode20MatVecRange96) panel11Mode20MatVecRange128) row

theorem panel11Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode21MatVecRange0) panel11Mode21MatVecRange32) panel11Mode21MatVecRange64) panel11Mode21MatVecRange96) panel11Mode21MatVecRange128) row

theorem panel11Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode22MatVecRange0) panel11Mode22MatVecRange32) panel11Mode22MatVecRange64) panel11Mode22MatVecRange96) panel11Mode22MatVecRange128) row

theorem panel11Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode23MatVecRange0) panel11Mode23MatVecRange32) panel11Mode23MatVecRange64) panel11Mode23MatVecRange96) panel11Mode23MatVecRange128) row

theorem panel11Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode24MatVecRange0) panel11Mode24MatVecRange32) panel11Mode24MatVecRange64) panel11Mode24MatVecRange96) panel11Mode24MatVecRange128) row

theorem panel11Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode25MatVecRange0) panel11Mode25MatVecRange32) panel11Mode25MatVecRange64) panel11Mode25MatVecRange96) panel11Mode25MatVecRange128) row

theorem panel11Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode26MatVecRange0) panel11Mode26MatVecRange32) panel11Mode26MatVecRange64) panel11Mode26MatVecRange96) panel11Mode26MatVecRange128) row

theorem panel11Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode27MatVecRange0) panel11Mode27MatVecRange32) panel11Mode27MatVecRange64) panel11Mode27MatVecRange96) panel11Mode27MatVecRange128) row

theorem panel11Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode28MatVecRange0) panel11Mode28MatVecRange32) panel11Mode28MatVecRange64) panel11Mode28MatVecRange96) panel11Mode28MatVecRange128) row

theorem panel11Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode29MatVecRange0) panel11Mode29MatVecRange32) panel11Mode29MatVecRange64) panel11Mode29MatVecRange96) panel11Mode29MatVecRange128) row

theorem panel11Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode30MatVecRange0) panel11Mode30MatVecRange32) panel11Mode30MatVecRange64) panel11Mode30MatVecRange96) panel11Mode30MatVecRange128) row

theorem panel11Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode31MatVecRange0) panel11Mode31MatVecRange32) panel11Mode31MatVecRange64) panel11Mode31MatVecRange96) panel11Mode31MatVecRange128) row

theorem panel11Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode32MatVecRange0) panel11Mode32MatVecRange32) panel11Mode32MatVecRange64) panel11Mode32MatVecRange96) panel11Mode32MatVecRange128) row

theorem panel11Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode33MatVecRange0) panel11Mode33MatVecRange32) panel11Mode33MatVecRange64) panel11Mode33MatVecRange96) panel11Mode33MatVecRange128) row

theorem panel11Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode34MatVecRange0) panel11Mode34MatVecRange32) panel11Mode34MatVecRange64) panel11Mode34MatVecRange96) panel11Mode34MatVecRange128) row

theorem panel11Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode35MatVecRange0) panel11Mode35MatVecRange32) panel11Mode35MatVecRange64) panel11Mode35MatVecRange96) panel11Mode35MatVecRange128) row

theorem panel11Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode36MatVecRange0) panel11Mode36MatVecRange32) panel11Mode36MatVecRange64) panel11Mode36MatVecRange96) panel11Mode36MatVecRange128) row

theorem panel11Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode37MatVecRange0) panel11Mode37MatVecRange32) panel11Mode37MatVecRange64) panel11Mode37MatVecRange96) panel11Mode37MatVecRange128) row

theorem panel11Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode38MatVecRange0) panel11Mode38MatVecRange32) panel11Mode38MatVecRange64) panel11Mode38MatVecRange96) panel11Mode38MatVecRange128) row

theorem panel11Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode39MatVecRange0) panel11Mode39MatVecRange32) panel11Mode39MatVecRange64) panel11Mode39MatVecRange96) panel11Mode39MatVecRange128) row

theorem panel11Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode40MatVecRange0) panel11Mode40MatVecRange32) panel11Mode40MatVecRange64) panel11Mode40MatVecRange96) panel11Mode40MatVecRange128) row

theorem panel11Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode41MatVecRange0) panel11Mode41MatVecRange32) panel11Mode41MatVecRange64) panel11Mode41MatVecRange96) panel11Mode41MatVecRange128) row

theorem panel11Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode42MatVecRange0) panel11Mode42MatVecRange32) panel11Mode42MatVecRange64) panel11Mode42MatVecRange96) panel11Mode42MatVecRange128) row

theorem panel11Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode43MatVecRange0) panel11Mode43MatVecRange32) panel11Mode43MatVecRange64) panel11Mode43MatVecRange96) panel11Mode43MatVecRange128) row

theorem panel11Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode44MatVecRange0) panel11Mode44MatVecRange32) panel11Mode44MatVecRange64) panel11Mode44MatVecRange96) panel11Mode44MatVecRange128) row

theorem panel11Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode45MatVecRange0) panel11Mode45MatVecRange32) panel11Mode45MatVecRange64) panel11Mode45MatVecRange96) panel11Mode45MatVecRange128) row

theorem panel11Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode46MatVecRange0) panel11Mode46MatVecRange32) panel11Mode46MatVecRange64) panel11Mode46MatVecRange96) panel11Mode46MatVecRange128) row

theorem panel11Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel11MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel11MomentData.moments
        (P2RoundedFactorCheckpointData.panel11FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel11Mode47MatVecRange0) panel11Mode47MatVecRange32) panel11Mode47MatVecRange64) panel11Mode47MatVecRange96) panel11Mode47MatVecRange128) row

theorem panel11MomentData_correct :
    P2RoundedFactorCheckpointData.panel11MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel11FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel11DefectMoments_eq panel11ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel11Mode0MatVec_eq
      · exact panel11Mode2MatVec_eq
      · exact panel11Mode4MatVec_eq
      · exact panel11Mode6MatVec_eq
      · exact panel11Mode8MatVec_eq
      · exact panel11Mode10MatVec_eq
      · exact panel11Mode12MatVec_eq
      · exact panel11Mode14MatVec_eq
      · exact panel11Mode16MatVec_eq
      · exact panel11Mode18MatVec_eq
      · exact panel11Mode20MatVec_eq
      · exact panel11Mode22MatVec_eq
      · exact panel11Mode24MatVec_eq
      · exact panel11Mode26MatVec_eq
      · exact panel11Mode28MatVec_eq
      · exact panel11Mode30MatVec_eq
      · exact panel11Mode32MatVec_eq
      · exact panel11Mode34MatVec_eq
      · exact panel11Mode36MatVec_eq
      · exact panel11Mode38MatVec_eq
      · exact panel11Mode40MatVec_eq
      · exact panel11Mode42MatVec_eq
      · exact panel11Mode44MatVec_eq
      · exact panel11Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel11Mode1MatVec_eq
      · exact panel11Mode3MatVec_eq
      · exact panel11Mode5MatVec_eq
      · exact panel11Mode7MatVec_eq
      · exact panel11Mode9MatVec_eq
      · exact panel11Mode11MatVec_eq
      · exact panel11Mode13MatVec_eq
      · exact panel11Mode15MatVec_eq
      · exact panel11Mode17MatVec_eq
      · exact panel11Mode19MatVec_eq
      · exact panel11Mode21MatVec_eq
      · exact panel11Mode23MatVec_eq
      · exact panel11Mode25MatVec_eq
      · exact panel11Mode27MatVec_eq
      · exact panel11Mode29MatVec_eq
      · exact panel11Mode31MatVec_eq
      · exact panel11Mode33MatVec_eq
      · exact panel11Mode35MatVec_eq
      · exact panel11Mode37MatVec_eq
      · exact panel11Mode39MatVec_eq
      · exact panel11Mode41MatVec_eq
      · exact panel11Mode43MatVec_eq
      · exact panel11Mode45MatVec_eq
      · exact panel11Mode47MatVec_eq

end RHP2Bridge
