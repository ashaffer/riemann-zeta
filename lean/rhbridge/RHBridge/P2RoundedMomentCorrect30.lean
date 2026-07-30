import RHBridge.P2RoundedFlatFactorCheckpoint30
import RHBridge.P2RoundedMomentLengths30
import RHBridge.P2RoundedMomentCheckpointCheck30_moments
import RHBridge.P2RoundedMomentCheckpointCheck30_mode0
import RHBridge.P2RoundedMomentCheckpointCheck30_mode1
import RHBridge.P2RoundedMomentCheckpointCheck30_mode2
import RHBridge.P2RoundedMomentCheckpointCheck30_mode3
import RHBridge.P2RoundedMomentCheckpointCheck30_mode4
import RHBridge.P2RoundedMomentCheckpointCheck30_mode5
import RHBridge.P2RoundedMomentCheckpointCheck30_mode6
import RHBridge.P2RoundedMomentCheckpointCheck30_mode7
import RHBridge.P2RoundedMomentCheckpointCheck30_mode8
import RHBridge.P2RoundedMomentCheckpointCheck30_mode9
import RHBridge.P2RoundedMomentCheckpointCheck30_mode10
import RHBridge.P2RoundedMomentCheckpointCheck30_mode11
import RHBridge.P2RoundedMomentCheckpointCheck30_mode12
import RHBridge.P2RoundedMomentCheckpointCheck30_mode13
import RHBridge.P2RoundedMomentCheckpointCheck30_mode14
import RHBridge.P2RoundedMomentCheckpointCheck30_mode15
import RHBridge.P2RoundedMomentCheckpointCheck30_mode16
import RHBridge.P2RoundedMomentCheckpointCheck30_mode17
import RHBridge.P2RoundedMomentCheckpointCheck30_mode18
import RHBridge.P2RoundedMomentCheckpointCheck30_mode19
import RHBridge.P2RoundedMomentCheckpointCheck30_mode20
import RHBridge.P2RoundedMomentCheckpointCheck30_mode21
import RHBridge.P2RoundedMomentCheckpointCheck30_mode22
import RHBridge.P2RoundedMomentCheckpointCheck30_mode23
import RHBridge.P2RoundedMomentCheckpointCheck30_mode24
import RHBridge.P2RoundedMomentCheckpointCheck30_mode25
import RHBridge.P2RoundedMomentCheckpointCheck30_mode26
import RHBridge.P2RoundedMomentCheckpointCheck30_mode27
import RHBridge.P2RoundedMomentCheckpointCheck30_mode28
import RHBridge.P2RoundedMomentCheckpointCheck30_mode29
import RHBridge.P2RoundedMomentCheckpointCheck30_mode30
import RHBridge.P2RoundedMomentCheckpointCheck30_mode31
import RHBridge.P2RoundedMomentCheckpointCheck30_mode32
import RHBridge.P2RoundedMomentCheckpointCheck30_mode33
import RHBridge.P2RoundedMomentCheckpointCheck30_mode34
import RHBridge.P2RoundedMomentCheckpointCheck30_mode35
import RHBridge.P2RoundedMomentCheckpointCheck30_mode36
import RHBridge.P2RoundedMomentCheckpointCheck30_mode37
import RHBridge.P2RoundedMomentCheckpointCheck30_mode38
import RHBridge.P2RoundedMomentCheckpointCheck30_mode39
import RHBridge.P2RoundedMomentCheckpointCheck30_mode40
import RHBridge.P2RoundedMomentCheckpointCheck30_mode41
import RHBridge.P2RoundedMomentCheckpointCheck30_mode42
import RHBridge.P2RoundedMomentCheckpointCheck30_mode43
import RHBridge.P2RoundedMomentCheckpointCheck30_mode44
import RHBridge.P2RoundedMomentCheckpointCheck30_mode45
import RHBridge.P2RoundedMomentCheckpointCheck30_mode46
import RHBridge.P2RoundedMomentCheckpointCheck30_mode47

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

theorem panel30DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel30FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30DefectMomentRange0) panel30DefectMomentRange64) panel30DefectMomentRange128) panel30DefectMomentRange192) panel30DefectMomentRange256) row

theorem panel30Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode0MatVecRange0) panel30Mode0MatVecRange32) panel30Mode0MatVecRange64) panel30Mode0MatVecRange96) panel30Mode0MatVecRange128) row

theorem panel30Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode1MatVecRange0) panel30Mode1MatVecRange32) panel30Mode1MatVecRange64) panel30Mode1MatVecRange96) panel30Mode1MatVecRange128) row

theorem panel30Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode2MatVecRange0) panel30Mode2MatVecRange32) panel30Mode2MatVecRange64) panel30Mode2MatVecRange96) panel30Mode2MatVecRange128) row

theorem panel30Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode3MatVecRange0) panel30Mode3MatVecRange32) panel30Mode3MatVecRange64) panel30Mode3MatVecRange96) panel30Mode3MatVecRange128) row

theorem panel30Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode4MatVecRange0) panel30Mode4MatVecRange32) panel30Mode4MatVecRange64) panel30Mode4MatVecRange96) panel30Mode4MatVecRange128) row

theorem panel30Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode5MatVecRange0) panel30Mode5MatVecRange32) panel30Mode5MatVecRange64) panel30Mode5MatVecRange96) panel30Mode5MatVecRange128) row

theorem panel30Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode6MatVecRange0) panel30Mode6MatVecRange32) panel30Mode6MatVecRange64) panel30Mode6MatVecRange96) panel30Mode6MatVecRange128) row

theorem panel30Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode7MatVecRange0) panel30Mode7MatVecRange32) panel30Mode7MatVecRange64) panel30Mode7MatVecRange96) panel30Mode7MatVecRange128) row

theorem panel30Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode8MatVecRange0) panel30Mode8MatVecRange32) panel30Mode8MatVecRange64) panel30Mode8MatVecRange96) panel30Mode8MatVecRange128) row

theorem panel30Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode9MatVecRange0) panel30Mode9MatVecRange32) panel30Mode9MatVecRange64) panel30Mode9MatVecRange96) panel30Mode9MatVecRange128) row

theorem panel30Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode10MatVecRange0) panel30Mode10MatVecRange32) panel30Mode10MatVecRange64) panel30Mode10MatVecRange96) panel30Mode10MatVecRange128) row

theorem panel30Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode11MatVecRange0) panel30Mode11MatVecRange32) panel30Mode11MatVecRange64) panel30Mode11MatVecRange96) panel30Mode11MatVecRange128) row

theorem panel30Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode12MatVecRange0) panel30Mode12MatVecRange32) panel30Mode12MatVecRange64) panel30Mode12MatVecRange96) panel30Mode12MatVecRange128) row

theorem panel30Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode13MatVecRange0) panel30Mode13MatVecRange32) panel30Mode13MatVecRange64) panel30Mode13MatVecRange96) panel30Mode13MatVecRange128) row

theorem panel30Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode14MatVecRange0) panel30Mode14MatVecRange32) panel30Mode14MatVecRange64) panel30Mode14MatVecRange96) panel30Mode14MatVecRange128) row

theorem panel30Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode15MatVecRange0) panel30Mode15MatVecRange32) panel30Mode15MatVecRange64) panel30Mode15MatVecRange96) panel30Mode15MatVecRange128) row

theorem panel30Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode16MatVecRange0) panel30Mode16MatVecRange32) panel30Mode16MatVecRange64) panel30Mode16MatVecRange96) panel30Mode16MatVecRange128) row

theorem panel30Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode17MatVecRange0) panel30Mode17MatVecRange32) panel30Mode17MatVecRange64) panel30Mode17MatVecRange96) panel30Mode17MatVecRange128) row

theorem panel30Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode18MatVecRange0) panel30Mode18MatVecRange32) panel30Mode18MatVecRange64) panel30Mode18MatVecRange96) panel30Mode18MatVecRange128) row

theorem panel30Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode19MatVecRange0) panel30Mode19MatVecRange32) panel30Mode19MatVecRange64) panel30Mode19MatVecRange96) panel30Mode19MatVecRange128) row

theorem panel30Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode20MatVecRange0) panel30Mode20MatVecRange32) panel30Mode20MatVecRange64) panel30Mode20MatVecRange96) panel30Mode20MatVecRange128) row

theorem panel30Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode21MatVecRange0) panel30Mode21MatVecRange32) panel30Mode21MatVecRange64) panel30Mode21MatVecRange96) panel30Mode21MatVecRange128) row

theorem panel30Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode22MatVecRange0) panel30Mode22MatVecRange32) panel30Mode22MatVecRange64) panel30Mode22MatVecRange96) panel30Mode22MatVecRange128) row

theorem panel30Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode23MatVecRange0) panel30Mode23MatVecRange32) panel30Mode23MatVecRange64) panel30Mode23MatVecRange96) panel30Mode23MatVecRange128) row

theorem panel30Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode24MatVecRange0) panel30Mode24MatVecRange32) panel30Mode24MatVecRange64) panel30Mode24MatVecRange96) panel30Mode24MatVecRange128) row

theorem panel30Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode25MatVecRange0) panel30Mode25MatVecRange32) panel30Mode25MatVecRange64) panel30Mode25MatVecRange96) panel30Mode25MatVecRange128) row

theorem panel30Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode26MatVecRange0) panel30Mode26MatVecRange32) panel30Mode26MatVecRange64) panel30Mode26MatVecRange96) panel30Mode26MatVecRange128) row

theorem panel30Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode27MatVecRange0) panel30Mode27MatVecRange32) panel30Mode27MatVecRange64) panel30Mode27MatVecRange96) panel30Mode27MatVecRange128) row

theorem panel30Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode28MatVecRange0) panel30Mode28MatVecRange32) panel30Mode28MatVecRange64) panel30Mode28MatVecRange96) panel30Mode28MatVecRange128) row

theorem panel30Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode29MatVecRange0) panel30Mode29MatVecRange32) panel30Mode29MatVecRange64) panel30Mode29MatVecRange96) panel30Mode29MatVecRange128) row

theorem panel30Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode30MatVecRange0) panel30Mode30MatVecRange32) panel30Mode30MatVecRange64) panel30Mode30MatVecRange96) panel30Mode30MatVecRange128) row

theorem panel30Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode31MatVecRange0) panel30Mode31MatVecRange32) panel30Mode31MatVecRange64) panel30Mode31MatVecRange96) panel30Mode31MatVecRange128) row

theorem panel30Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode32MatVecRange0) panel30Mode32MatVecRange32) panel30Mode32MatVecRange64) panel30Mode32MatVecRange96) panel30Mode32MatVecRange128) row

theorem panel30Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode33MatVecRange0) panel30Mode33MatVecRange32) panel30Mode33MatVecRange64) panel30Mode33MatVecRange96) panel30Mode33MatVecRange128) row

theorem panel30Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode34MatVecRange0) panel30Mode34MatVecRange32) panel30Mode34MatVecRange64) panel30Mode34MatVecRange96) panel30Mode34MatVecRange128) row

theorem panel30Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode35MatVecRange0) panel30Mode35MatVecRange32) panel30Mode35MatVecRange64) panel30Mode35MatVecRange96) panel30Mode35MatVecRange128) row

theorem panel30Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode36MatVecRange0) panel30Mode36MatVecRange32) panel30Mode36MatVecRange64) panel30Mode36MatVecRange96) panel30Mode36MatVecRange128) row

theorem panel30Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode37MatVecRange0) panel30Mode37MatVecRange32) panel30Mode37MatVecRange64) panel30Mode37MatVecRange96) panel30Mode37MatVecRange128) row

theorem panel30Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode38MatVecRange0) panel30Mode38MatVecRange32) panel30Mode38MatVecRange64) panel30Mode38MatVecRange96) panel30Mode38MatVecRange128) row

theorem panel30Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode39MatVecRange0) panel30Mode39MatVecRange32) panel30Mode39MatVecRange64) panel30Mode39MatVecRange96) panel30Mode39MatVecRange128) row

theorem panel30Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode40MatVecRange0) panel30Mode40MatVecRange32) panel30Mode40MatVecRange64) panel30Mode40MatVecRange96) panel30Mode40MatVecRange128) row

theorem panel30Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode41MatVecRange0) panel30Mode41MatVecRange32) panel30Mode41MatVecRange64) panel30Mode41MatVecRange96) panel30Mode41MatVecRange128) row

theorem panel30Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode42MatVecRange0) panel30Mode42MatVecRange32) panel30Mode42MatVecRange64) panel30Mode42MatVecRange96) panel30Mode42MatVecRange128) row

theorem panel30Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode43MatVecRange0) panel30Mode43MatVecRange32) panel30Mode43MatVecRange64) panel30Mode43MatVecRange96) panel30Mode43MatVecRange128) row

theorem panel30Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode44MatVecRange0) panel30Mode44MatVecRange32) panel30Mode44MatVecRange64) panel30Mode44MatVecRange96) panel30Mode44MatVecRange128) row

theorem panel30Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode45MatVecRange0) panel30Mode45MatVecRange32) panel30Mode45MatVecRange64) panel30Mode45MatVecRange96) panel30Mode45MatVecRange128) row

theorem panel30Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode46MatVecRange0) panel30Mode46MatVecRange32) panel30Mode46MatVecRange64) panel30Mode46MatVecRange96) panel30Mode46MatVecRange128) row

theorem panel30Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel30MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel30MomentData.moments
        (P2RoundedFactorCheckpointData.panel30FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel30Mode47MatVecRange0) panel30Mode47MatVecRange32) panel30Mode47MatVecRange64) panel30Mode47MatVecRange96) panel30Mode47MatVecRange128) row

theorem panel30MomentData_correct :
    P2RoundedFactorCheckpointData.panel30MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel30FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel30DefectMoments_eq panel30ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel30Mode0MatVec_eq
      · exact panel30Mode2MatVec_eq
      · exact panel30Mode4MatVec_eq
      · exact panel30Mode6MatVec_eq
      · exact panel30Mode8MatVec_eq
      · exact panel30Mode10MatVec_eq
      · exact panel30Mode12MatVec_eq
      · exact panel30Mode14MatVec_eq
      · exact panel30Mode16MatVec_eq
      · exact panel30Mode18MatVec_eq
      · exact panel30Mode20MatVec_eq
      · exact panel30Mode22MatVec_eq
      · exact panel30Mode24MatVec_eq
      · exact panel30Mode26MatVec_eq
      · exact panel30Mode28MatVec_eq
      · exact panel30Mode30MatVec_eq
      · exact panel30Mode32MatVec_eq
      · exact panel30Mode34MatVec_eq
      · exact panel30Mode36MatVec_eq
      · exact panel30Mode38MatVec_eq
      · exact panel30Mode40MatVec_eq
      · exact panel30Mode42MatVec_eq
      · exact panel30Mode44MatVec_eq
      · exact panel30Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel30Mode1MatVec_eq
      · exact panel30Mode3MatVec_eq
      · exact panel30Mode5MatVec_eq
      · exact panel30Mode7MatVec_eq
      · exact panel30Mode9MatVec_eq
      · exact panel30Mode11MatVec_eq
      · exact panel30Mode13MatVec_eq
      · exact panel30Mode15MatVec_eq
      · exact panel30Mode17MatVec_eq
      · exact panel30Mode19MatVec_eq
      · exact panel30Mode21MatVec_eq
      · exact panel30Mode23MatVec_eq
      · exact panel30Mode25MatVec_eq
      · exact panel30Mode27MatVec_eq
      · exact panel30Mode29MatVec_eq
      · exact panel30Mode31MatVec_eq
      · exact panel30Mode33MatVec_eq
      · exact panel30Mode35MatVec_eq
      · exact panel30Mode37MatVec_eq
      · exact panel30Mode39MatVec_eq
      · exact panel30Mode41MatVec_eq
      · exact panel30Mode43MatVec_eq
      · exact panel30Mode45MatVec_eq
      · exact panel30Mode47MatVec_eq

end RHP2Bridge
