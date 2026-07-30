import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk3 :
    P2RoundedFactorCheckpointData.panel19Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix12_eq :
    P2RoundedFactorCheckpointData.panel19Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk3.1

theorem panel19Prefix13_eq :
    P2RoundedFactorCheckpointData.panel19Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk3.2.1

theorem panel19Prefix14_eq :
    P2RoundedFactorCheckpointData.panel19Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk3.2.2.1

theorem panel19Prefix15_eq :
    P2RoundedFactorCheckpointData.panel19Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk3.2.2.2

end RHP2Bridge
