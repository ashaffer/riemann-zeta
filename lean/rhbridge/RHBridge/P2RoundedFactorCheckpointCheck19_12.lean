import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk12 :
    P2RoundedFactorCheckpointData.panel19Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix48_eq :
    P2RoundedFactorCheckpointData.panel19Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk12.1

theorem panel19Prefix49_eq :
    P2RoundedFactorCheckpointData.panel19Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk12.2.1

theorem panel19Prefix50_eq :
    P2RoundedFactorCheckpointData.panel19Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk12.2.2.1

theorem panel19Prefix51_eq :
    P2RoundedFactorCheckpointData.panel19Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk12.2.2.2

end RHP2Bridge
