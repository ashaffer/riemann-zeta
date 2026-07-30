import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk13 :
    P2RoundedFactorCheckpointData.panel19Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix52_eq :
    P2RoundedFactorCheckpointData.panel19Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk13.1

theorem panel19Prefix53_eq :
    P2RoundedFactorCheckpointData.panel19Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk13.2.1

theorem panel19Prefix54_eq :
    P2RoundedFactorCheckpointData.panel19Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk13.2.2.1

theorem panel19Prefix55_eq :
    P2RoundedFactorCheckpointData.panel19Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk13.2.2.2

end RHP2Bridge
