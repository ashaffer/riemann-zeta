import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk13 :
    P2RoundedFactorCheckpointData.panel20Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix52_eq :
    P2RoundedFactorCheckpointData.panel20Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk13.1

theorem panel20Prefix53_eq :
    P2RoundedFactorCheckpointData.panel20Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk13.2.1

theorem panel20Prefix54_eq :
    P2RoundedFactorCheckpointData.panel20Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk13.2.2.1

theorem panel20Prefix55_eq :
    P2RoundedFactorCheckpointData.panel20Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk13.2.2.2

end RHP2Bridge
