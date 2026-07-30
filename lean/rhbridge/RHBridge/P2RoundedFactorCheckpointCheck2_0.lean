import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk0 :
    P2RoundedFactorCheckpointData.panel2Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix0_eq :
    P2RoundedFactorCheckpointData.panel2Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk0.1

theorem panel2Prefix1_eq :
    P2RoundedFactorCheckpointData.panel2Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk0.2.1

theorem panel2Prefix2_eq :
    P2RoundedFactorCheckpointData.panel2Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk0.2.2.1

theorem panel2Prefix3_eq :
    P2RoundedFactorCheckpointData.panel2Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk0.2.2.2

end RHP2Bridge
