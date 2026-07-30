import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk8 :
    P2RoundedFactorCheckpointData.panel19Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix32_eq :
    P2RoundedFactorCheckpointData.panel19Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk8.1

theorem panel19Prefix33_eq :
    P2RoundedFactorCheckpointData.panel19Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk8.2.1

theorem panel19Prefix34_eq :
    P2RoundedFactorCheckpointData.panel19Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk8.2.2.1

theorem panel19Prefix35_eq :
    P2RoundedFactorCheckpointData.panel19Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk8.2.2.2

end RHP2Bridge
