import RHBridge.P2RoundedFlatFactorCheckpoint19
import RHBridge.P2RoundedMomentLengths19
import RHBridge.P2RoundedMomentCheckpointCheck19_moments
import RHBridge.P2RoundedMomentCheckpointCheck19_mode0
import RHBridge.P2RoundedMomentCheckpointCheck19_mode1
import RHBridge.P2RoundedMomentCheckpointCheck19_mode2
import RHBridge.P2RoundedMomentCheckpointCheck19_mode3
import RHBridge.P2RoundedMomentCheckpointCheck19_mode4
import RHBridge.P2RoundedMomentCheckpointCheck19_mode5
import RHBridge.P2RoundedMomentCheckpointCheck19_mode6
import RHBridge.P2RoundedMomentCheckpointCheck19_mode7
import RHBridge.P2RoundedMomentCheckpointCheck19_mode8
import RHBridge.P2RoundedMomentCheckpointCheck19_mode9
import RHBridge.P2RoundedMomentCheckpointCheck19_mode10
import RHBridge.P2RoundedMomentCheckpointCheck19_mode11
import RHBridge.P2RoundedMomentCheckpointCheck19_mode12
import RHBridge.P2RoundedMomentCheckpointCheck19_mode13
import RHBridge.P2RoundedMomentCheckpointCheck19_mode14
import RHBridge.P2RoundedMomentCheckpointCheck19_mode15
import RHBridge.P2RoundedMomentCheckpointCheck19_mode16
import RHBridge.P2RoundedMomentCheckpointCheck19_mode17
import RHBridge.P2RoundedMomentCheckpointCheck19_mode18
import RHBridge.P2RoundedMomentCheckpointCheck19_mode19
import RHBridge.P2RoundedMomentCheckpointCheck19_mode20
import RHBridge.P2RoundedMomentCheckpointCheck19_mode21
import RHBridge.P2RoundedMomentCheckpointCheck19_mode22
import RHBridge.P2RoundedMomentCheckpointCheck19_mode23
import RHBridge.P2RoundedMomentCheckpointCheck19_mode24
import RHBridge.P2RoundedMomentCheckpointCheck19_mode25
import RHBridge.P2RoundedMomentCheckpointCheck19_mode26
import RHBridge.P2RoundedMomentCheckpointCheck19_mode27
import RHBridge.P2RoundedMomentCheckpointCheck19_mode28
import RHBridge.P2RoundedMomentCheckpointCheck19_mode29
import RHBridge.P2RoundedMomentCheckpointCheck19_mode30
import RHBridge.P2RoundedMomentCheckpointCheck19_mode31
import RHBridge.P2RoundedMomentCheckpointCheck19_mode32
import RHBridge.P2RoundedMomentCheckpointCheck19_mode33
import RHBridge.P2RoundedMomentCheckpointCheck19_mode34
import RHBridge.P2RoundedMomentCheckpointCheck19_mode35
import RHBridge.P2RoundedMomentCheckpointCheck19_mode36
import RHBridge.P2RoundedMomentCheckpointCheck19_mode37
import RHBridge.P2RoundedMomentCheckpointCheck19_mode38
import RHBridge.P2RoundedMomentCheckpointCheck19_mode39
import RHBridge.P2RoundedMomentCheckpointCheck19_mode40
import RHBridge.P2RoundedMomentCheckpointCheck19_mode41
import RHBridge.P2RoundedMomentCheckpointCheck19_mode42
import RHBridge.P2RoundedMomentCheckpointCheck19_mode43
import RHBridge.P2RoundedMomentCheckpointCheck19_mode44
import RHBridge.P2RoundedMomentCheckpointCheck19_mode45
import RHBridge.P2RoundedMomentCheckpointCheck19_mode46
import RHBridge.P2RoundedMomentCheckpointCheck19_mode47

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

theorem panel19DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel19FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19DefectMomentRange0) panel19DefectMomentRange64) panel19DefectMomentRange128) panel19DefectMomentRange192) panel19DefectMomentRange256) row

theorem panel19Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode0MatVecRange0) panel19Mode0MatVecRange32) panel19Mode0MatVecRange64) panel19Mode0MatVecRange96) panel19Mode0MatVecRange128) row

theorem panel19Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode1MatVecRange0) panel19Mode1MatVecRange32) panel19Mode1MatVecRange64) panel19Mode1MatVecRange96) panel19Mode1MatVecRange128) row

theorem panel19Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode2MatVecRange0) panel19Mode2MatVecRange32) panel19Mode2MatVecRange64) panel19Mode2MatVecRange96) panel19Mode2MatVecRange128) row

theorem panel19Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode3MatVecRange0) panel19Mode3MatVecRange32) panel19Mode3MatVecRange64) panel19Mode3MatVecRange96) panel19Mode3MatVecRange128) row

theorem panel19Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode4MatVecRange0) panel19Mode4MatVecRange32) panel19Mode4MatVecRange64) panel19Mode4MatVecRange96) panel19Mode4MatVecRange128) row

theorem panel19Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode5MatVecRange0) panel19Mode5MatVecRange32) panel19Mode5MatVecRange64) panel19Mode5MatVecRange96) panel19Mode5MatVecRange128) row

theorem panel19Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode6MatVecRange0) panel19Mode6MatVecRange32) panel19Mode6MatVecRange64) panel19Mode6MatVecRange96) panel19Mode6MatVecRange128) row

theorem panel19Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode7MatVecRange0) panel19Mode7MatVecRange32) panel19Mode7MatVecRange64) panel19Mode7MatVecRange96) panel19Mode7MatVecRange128) row

theorem panel19Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode8MatVecRange0) panel19Mode8MatVecRange32) panel19Mode8MatVecRange64) panel19Mode8MatVecRange96) panel19Mode8MatVecRange128) row

theorem panel19Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode9MatVecRange0) panel19Mode9MatVecRange32) panel19Mode9MatVecRange64) panel19Mode9MatVecRange96) panel19Mode9MatVecRange128) row

theorem panel19Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode10MatVecRange0) panel19Mode10MatVecRange32) panel19Mode10MatVecRange64) panel19Mode10MatVecRange96) panel19Mode10MatVecRange128) row

theorem panel19Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode11MatVecRange0) panel19Mode11MatVecRange32) panel19Mode11MatVecRange64) panel19Mode11MatVecRange96) panel19Mode11MatVecRange128) row

theorem panel19Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode12MatVecRange0) panel19Mode12MatVecRange32) panel19Mode12MatVecRange64) panel19Mode12MatVecRange96) panel19Mode12MatVecRange128) row

theorem panel19Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode13MatVecRange0) panel19Mode13MatVecRange32) panel19Mode13MatVecRange64) panel19Mode13MatVecRange96) panel19Mode13MatVecRange128) row

theorem panel19Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode14MatVecRange0) panel19Mode14MatVecRange32) panel19Mode14MatVecRange64) panel19Mode14MatVecRange96) panel19Mode14MatVecRange128) row

theorem panel19Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode15MatVecRange0) panel19Mode15MatVecRange32) panel19Mode15MatVecRange64) panel19Mode15MatVecRange96) panel19Mode15MatVecRange128) row

theorem panel19Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode16MatVecRange0) panel19Mode16MatVecRange32) panel19Mode16MatVecRange64) panel19Mode16MatVecRange96) panel19Mode16MatVecRange128) row

theorem panel19Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode17MatVecRange0) panel19Mode17MatVecRange32) panel19Mode17MatVecRange64) panel19Mode17MatVecRange96) panel19Mode17MatVecRange128) row

theorem panel19Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode18MatVecRange0) panel19Mode18MatVecRange32) panel19Mode18MatVecRange64) panel19Mode18MatVecRange96) panel19Mode18MatVecRange128) row

theorem panel19Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode19MatVecRange0) panel19Mode19MatVecRange32) panel19Mode19MatVecRange64) panel19Mode19MatVecRange96) panel19Mode19MatVecRange128) row

theorem panel19Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode20MatVecRange0) panel19Mode20MatVecRange32) panel19Mode20MatVecRange64) panel19Mode20MatVecRange96) panel19Mode20MatVecRange128) row

theorem panel19Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode21MatVecRange0) panel19Mode21MatVecRange32) panel19Mode21MatVecRange64) panel19Mode21MatVecRange96) panel19Mode21MatVecRange128) row

theorem panel19Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode22MatVecRange0) panel19Mode22MatVecRange32) panel19Mode22MatVecRange64) panel19Mode22MatVecRange96) panel19Mode22MatVecRange128) row

theorem panel19Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode23MatVecRange0) panel19Mode23MatVecRange32) panel19Mode23MatVecRange64) panel19Mode23MatVecRange96) panel19Mode23MatVecRange128) row

theorem panel19Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode24MatVecRange0) panel19Mode24MatVecRange32) panel19Mode24MatVecRange64) panel19Mode24MatVecRange96) panel19Mode24MatVecRange128) row

theorem panel19Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode25MatVecRange0) panel19Mode25MatVecRange32) panel19Mode25MatVecRange64) panel19Mode25MatVecRange96) panel19Mode25MatVecRange128) row

theorem panel19Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode26MatVecRange0) panel19Mode26MatVecRange32) panel19Mode26MatVecRange64) panel19Mode26MatVecRange96) panel19Mode26MatVecRange128) row

theorem panel19Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode27MatVecRange0) panel19Mode27MatVecRange32) panel19Mode27MatVecRange64) panel19Mode27MatVecRange96) panel19Mode27MatVecRange128) row

theorem panel19Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode28MatVecRange0) panel19Mode28MatVecRange32) panel19Mode28MatVecRange64) panel19Mode28MatVecRange96) panel19Mode28MatVecRange128) row

theorem panel19Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode29MatVecRange0) panel19Mode29MatVecRange32) panel19Mode29MatVecRange64) panel19Mode29MatVecRange96) panel19Mode29MatVecRange128) row

theorem panel19Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode30MatVecRange0) panel19Mode30MatVecRange32) panel19Mode30MatVecRange64) panel19Mode30MatVecRange96) panel19Mode30MatVecRange128) row

theorem panel19Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode31MatVecRange0) panel19Mode31MatVecRange32) panel19Mode31MatVecRange64) panel19Mode31MatVecRange96) panel19Mode31MatVecRange128) row

theorem panel19Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode32MatVecRange0) panel19Mode32MatVecRange32) panel19Mode32MatVecRange64) panel19Mode32MatVecRange96) panel19Mode32MatVecRange128) row

theorem panel19Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode33MatVecRange0) panel19Mode33MatVecRange32) panel19Mode33MatVecRange64) panel19Mode33MatVecRange96) panel19Mode33MatVecRange128) row

theorem panel19Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode34MatVecRange0) panel19Mode34MatVecRange32) panel19Mode34MatVecRange64) panel19Mode34MatVecRange96) panel19Mode34MatVecRange128) row

theorem panel19Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode35MatVecRange0) panel19Mode35MatVecRange32) panel19Mode35MatVecRange64) panel19Mode35MatVecRange96) panel19Mode35MatVecRange128) row

theorem panel19Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode36MatVecRange0) panel19Mode36MatVecRange32) panel19Mode36MatVecRange64) panel19Mode36MatVecRange96) panel19Mode36MatVecRange128) row

theorem panel19Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode37MatVecRange0) panel19Mode37MatVecRange32) panel19Mode37MatVecRange64) panel19Mode37MatVecRange96) panel19Mode37MatVecRange128) row

theorem panel19Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode38MatVecRange0) panel19Mode38MatVecRange32) panel19Mode38MatVecRange64) panel19Mode38MatVecRange96) panel19Mode38MatVecRange128) row

theorem panel19Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode39MatVecRange0) panel19Mode39MatVecRange32) panel19Mode39MatVecRange64) panel19Mode39MatVecRange96) panel19Mode39MatVecRange128) row

theorem panel19Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode40MatVecRange0) panel19Mode40MatVecRange32) panel19Mode40MatVecRange64) panel19Mode40MatVecRange96) panel19Mode40MatVecRange128) row

theorem panel19Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode41MatVecRange0) panel19Mode41MatVecRange32) panel19Mode41MatVecRange64) panel19Mode41MatVecRange96) panel19Mode41MatVecRange128) row

theorem panel19Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode42MatVecRange0) panel19Mode42MatVecRange32) panel19Mode42MatVecRange64) panel19Mode42MatVecRange96) panel19Mode42MatVecRange128) row

theorem panel19Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode43MatVecRange0) panel19Mode43MatVecRange32) panel19Mode43MatVecRange64) panel19Mode43MatVecRange96) panel19Mode43MatVecRange128) row

theorem panel19Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode44MatVecRange0) panel19Mode44MatVecRange32) panel19Mode44MatVecRange64) panel19Mode44MatVecRange96) panel19Mode44MatVecRange128) row

theorem panel19Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode45MatVecRange0) panel19Mode45MatVecRange32) panel19Mode45MatVecRange64) panel19Mode45MatVecRange96) panel19Mode45MatVecRange128) row

theorem panel19Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode46MatVecRange0) panel19Mode46MatVecRange32) panel19Mode46MatVecRange64) panel19Mode46MatVecRange96) panel19Mode46MatVecRange128) row

theorem panel19Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel19MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel19MomentData.moments
        (P2RoundedFactorCheckpointData.panel19FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel19Mode47MatVecRange0) panel19Mode47MatVecRange32) panel19Mode47MatVecRange64) panel19Mode47MatVecRange96) panel19Mode47MatVecRange128) row

theorem panel19MomentData_correct :
    P2RoundedFactorCheckpointData.panel19MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel19FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel19DefectMoments_eq panel19ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel19Mode0MatVec_eq
      · exact panel19Mode2MatVec_eq
      · exact panel19Mode4MatVec_eq
      · exact panel19Mode6MatVec_eq
      · exact panel19Mode8MatVec_eq
      · exact panel19Mode10MatVec_eq
      · exact panel19Mode12MatVec_eq
      · exact panel19Mode14MatVec_eq
      · exact panel19Mode16MatVec_eq
      · exact panel19Mode18MatVec_eq
      · exact panel19Mode20MatVec_eq
      · exact panel19Mode22MatVec_eq
      · exact panel19Mode24MatVec_eq
      · exact panel19Mode26MatVec_eq
      · exact panel19Mode28MatVec_eq
      · exact panel19Mode30MatVec_eq
      · exact panel19Mode32MatVec_eq
      · exact panel19Mode34MatVec_eq
      · exact panel19Mode36MatVec_eq
      · exact panel19Mode38MatVec_eq
      · exact panel19Mode40MatVec_eq
      · exact panel19Mode42MatVec_eq
      · exact panel19Mode44MatVec_eq
      · exact panel19Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel19Mode1MatVec_eq
      · exact panel19Mode3MatVec_eq
      · exact panel19Mode5MatVec_eq
      · exact panel19Mode7MatVec_eq
      · exact panel19Mode9MatVec_eq
      · exact panel19Mode11MatVec_eq
      · exact panel19Mode13MatVec_eq
      · exact panel19Mode15MatVec_eq
      · exact panel19Mode17MatVec_eq
      · exact panel19Mode19MatVec_eq
      · exact panel19Mode21MatVec_eq
      · exact panel19Mode23MatVec_eq
      · exact panel19Mode25MatVec_eq
      · exact panel19Mode27MatVec_eq
      · exact panel19Mode29MatVec_eq
      · exact panel19Mode31MatVec_eq
      · exact panel19Mode33MatVec_eq
      · exact panel19Mode35MatVec_eq
      · exact panel19Mode37MatVec_eq
      · exact panel19Mode39MatVec_eq
      · exact panel19Mode41MatVec_eq
      · exact panel19Mode43MatVec_eq
      · exact panel19Mode45MatVec_eq
      · exact panel19Mode47MatVec_eq

end RHP2Bridge
