import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk0 :
    P2RoundedFactorCheckpointData.panel14Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix0_eq :
    P2RoundedFactorCheckpointData.panel14Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk0.1

theorem panel14Prefix1_eq :
    P2RoundedFactorCheckpointData.panel14Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk0.2.1

theorem panel14Prefix2_eq :
    P2RoundedFactorCheckpointData.panel14Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk0.2.2.1

theorem panel14Prefix3_eq :
    P2RoundedFactorCheckpointData.panel14Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk0.2.2.2

end RHP2Bridge
