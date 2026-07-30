import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk0 :
    P2RoundedFactorCheckpointData.panel1Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix0_eq :
    P2RoundedFactorCheckpointData.panel1Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk0.1

theorem panel1Prefix1_eq :
    P2RoundedFactorCheckpointData.panel1Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk0.2.1

theorem panel1Prefix2_eq :
    P2RoundedFactorCheckpointData.panel1Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk0.2.2.1

theorem panel1Prefix3_eq :
    P2RoundedFactorCheckpointData.panel1Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk0.2.2.2

end RHP2Bridge
