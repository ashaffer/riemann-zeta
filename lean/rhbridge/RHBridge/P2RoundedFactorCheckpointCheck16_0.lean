import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk0 :
    P2RoundedFactorCheckpointData.panel16Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix0_eq :
    P2RoundedFactorCheckpointData.panel16Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk0.1

theorem panel16Prefix1_eq :
    P2RoundedFactorCheckpointData.panel16Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk0.2.1

theorem panel16Prefix2_eq :
    P2RoundedFactorCheckpointData.panel16Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk0.2.2.1

theorem panel16Prefix3_eq :
    P2RoundedFactorCheckpointData.panel16Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk0.2.2.2

end RHP2Bridge
