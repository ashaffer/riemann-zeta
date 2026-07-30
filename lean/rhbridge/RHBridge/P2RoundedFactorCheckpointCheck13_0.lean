import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk0 :
    P2RoundedFactorCheckpointData.panel13Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix0_eq :
    P2RoundedFactorCheckpointData.panel13Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk0.1

theorem panel13Prefix1_eq :
    P2RoundedFactorCheckpointData.panel13Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk0.2.1

theorem panel13Prefix2_eq :
    P2RoundedFactorCheckpointData.panel13Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk0.2.2.1

theorem panel13Prefix3_eq :
    P2RoundedFactorCheckpointData.panel13Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk0.2.2.2

end RHP2Bridge
