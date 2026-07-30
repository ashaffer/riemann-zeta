import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk15 :
    P2RoundedFactorCheckpointData.panel6Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix60_eq :
    P2RoundedFactorCheckpointData.panel6Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk15.1

theorem panel6Prefix61_eq :
    P2RoundedFactorCheckpointData.panel6Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk15.2.1

theorem panel6Prefix62_eq :
    P2RoundedFactorCheckpointData.panel6Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk15.2.2.1

theorem panel6Prefix63_eq :
    P2RoundedFactorCheckpointData.panel6Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk15.2.2.2

end RHP2Bridge
