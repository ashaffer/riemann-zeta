import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk5 :
    P2RoundedFactorCheckpointData.panel1Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix20_eq :
    P2RoundedFactorCheckpointData.panel1Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk5.1

theorem panel1Prefix21_eq :
    P2RoundedFactorCheckpointData.panel1Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk5.2.1

theorem panel1Prefix22_eq :
    P2RoundedFactorCheckpointData.panel1Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk5.2.2.1

theorem panel1Prefix23_eq :
    P2RoundedFactorCheckpointData.panel1Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk5.2.2.2

end RHP2Bridge
