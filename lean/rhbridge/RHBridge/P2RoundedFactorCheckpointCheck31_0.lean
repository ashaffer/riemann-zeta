import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk0 :
    P2RoundedFactorCheckpointData.panel31Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix0_eq :
    P2RoundedFactorCheckpointData.panel31Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk0.1

theorem panel31Prefix1_eq :
    P2RoundedFactorCheckpointData.panel31Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk0.2.1

theorem panel31Prefix2_eq :
    P2RoundedFactorCheckpointData.panel31Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk0.2.2.1

theorem panel31Prefix3_eq :
    P2RoundedFactorCheckpointData.panel31Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk0.2.2.2

end RHP2Bridge
