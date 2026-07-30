import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk0 :
    P2RoundedFactorCheckpointData.panel15Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix0_eq :
    P2RoundedFactorCheckpointData.panel15Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk0.1

theorem panel15Prefix1_eq :
    P2RoundedFactorCheckpointData.panel15Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk0.2.1

theorem panel15Prefix2_eq :
    P2RoundedFactorCheckpointData.panel15Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk0.2.2.1

theorem panel15Prefix3_eq :
    P2RoundedFactorCheckpointData.panel15Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk0.2.2.2

end RHP2Bridge
