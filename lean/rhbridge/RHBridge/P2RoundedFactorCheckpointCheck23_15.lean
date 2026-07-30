import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk15 :
    P2RoundedFactorCheckpointData.panel23Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix60_eq :
    P2RoundedFactorCheckpointData.panel23Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk15.1

theorem panel23Prefix61_eq :
    P2RoundedFactorCheckpointData.panel23Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk15.2.1

theorem panel23Prefix62_eq :
    P2RoundedFactorCheckpointData.panel23Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk15.2.2.1

theorem panel23Prefix63_eq :
    P2RoundedFactorCheckpointData.panel23Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk15.2.2.2

end RHP2Bridge
