import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk0 :
    P2RoundedFactorCheckpointData.panel6Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix0_eq :
    P2RoundedFactorCheckpointData.panel6Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk0.1

theorem panel6Prefix1_eq :
    P2RoundedFactorCheckpointData.panel6Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk0.2.1

theorem panel6Prefix2_eq :
    P2RoundedFactorCheckpointData.panel6Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk0.2.2.1

theorem panel6Prefix3_eq :
    P2RoundedFactorCheckpointData.panel6Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk0.2.2.2

end RHP2Bridge
