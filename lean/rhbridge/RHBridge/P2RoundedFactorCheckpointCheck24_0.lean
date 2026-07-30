import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk0 :
    P2RoundedFactorCheckpointData.panel24Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix0_eq :
    P2RoundedFactorCheckpointData.panel24Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk0.1

theorem panel24Prefix1_eq :
    P2RoundedFactorCheckpointData.panel24Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk0.2.1

theorem panel24Prefix2_eq :
    P2RoundedFactorCheckpointData.panel24Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk0.2.2.1

theorem panel24Prefix3_eq :
    P2RoundedFactorCheckpointData.panel24Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk0.2.2.2

end RHP2Bridge
