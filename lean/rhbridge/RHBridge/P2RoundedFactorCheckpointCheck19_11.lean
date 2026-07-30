import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk11 :
    P2RoundedFactorCheckpointData.panel19Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix44_eq :
    P2RoundedFactorCheckpointData.panel19Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk11.1

theorem panel19Prefix45_eq :
    P2RoundedFactorCheckpointData.panel19Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk11.2.1

theorem panel19Prefix46_eq :
    P2RoundedFactorCheckpointData.panel19Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk11.2.2.1

theorem panel19Prefix47_eq :
    P2RoundedFactorCheckpointData.panel19Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk11.2.2.2

end RHP2Bridge
