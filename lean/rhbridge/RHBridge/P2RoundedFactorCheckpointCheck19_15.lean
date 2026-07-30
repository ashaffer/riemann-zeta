import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk15 :
    P2RoundedFactorCheckpointData.panel19Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix60_eq :
    P2RoundedFactorCheckpointData.panel19Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk15.1

theorem panel19Prefix61_eq :
    P2RoundedFactorCheckpointData.panel19Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk15.2.1

theorem panel19Prefix62_eq :
    P2RoundedFactorCheckpointData.panel19Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk15.2.2.1

theorem panel19Prefix63_eq :
    P2RoundedFactorCheckpointData.panel19Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk15.2.2.2

end RHP2Bridge
