import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk15 :
    P2RoundedFactorCheckpointData.panel20Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix60_eq :
    P2RoundedFactorCheckpointData.panel20Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk15.1

theorem panel20Prefix61_eq :
    P2RoundedFactorCheckpointData.panel20Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk15.2.1

theorem panel20Prefix62_eq :
    P2RoundedFactorCheckpointData.panel20Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk15.2.2.1

theorem panel20Prefix63_eq :
    P2RoundedFactorCheckpointData.panel20Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk15.2.2.2

end RHP2Bridge
