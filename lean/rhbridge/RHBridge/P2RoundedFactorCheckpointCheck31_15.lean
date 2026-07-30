import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk15 :
    P2RoundedFactorCheckpointData.panel31Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix60_eq :
    P2RoundedFactorCheckpointData.panel31Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk15.1

theorem panel31Prefix61_eq :
    P2RoundedFactorCheckpointData.panel31Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk15.2.1

theorem panel31Prefix62_eq :
    P2RoundedFactorCheckpointData.panel31Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk15.2.2.1

theorem panel31Prefix63_eq :
    P2RoundedFactorCheckpointData.panel31Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk15.2.2.2

end RHP2Bridge
